package tech.burny.cloud.auth;

@SpringBootApplication(scanBasePackages = "tech.burny.cloud")
public class AuthApplication {
    public static void main(String[] args) {
        SpringApplication.run(Application.class,args);
    }
}