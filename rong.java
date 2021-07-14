import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.Chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import static org.openqa.selenium.support.ui.ExpectedConditions.presenceOfElementLocated;
import java.time.Duration;

public class HelloSelenium {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://www6.vghtpe.gov.tw/reg/c19vaccLine.do");
            driver.findElement(By.name("linename")).sendKeys("");
            driver.findElement(By.name("phone")).sendKeys("");
            driver.findElement(By.name("lineid")).sendKeys("");


            WebDriverWait wait = new WebDriverWait(driver,5);
        } finally {
            driver.quit();
        }
    }
}
