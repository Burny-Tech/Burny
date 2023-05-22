package cloud.tech.burny;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author cyx
 * @note
 * @date 2023/5/22 23:17
 */
@SpringBootApplication(scanBasePackages = "cloud.tech.burny")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class,args);
    }
}
