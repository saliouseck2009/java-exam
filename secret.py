722a3620101c452ab0404279b5066e4c
this may also be found at: /var/jenkins_home/secrets/initialAdminPassword




echo "# java-exam" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/saliouseck2009/java-exam.git
git push -u origin main



version: '2'

services:

  jenkins:
    image: jenkins/jenkins:lts
    volumes:
       - jenkins_data:/var/jenkins_home
    networks:
      - sonarnet
    ports:
      - '8080:8080'
      - '50000:50000'

  sonarqube:
    image: sonarqube:7.6-community 
    volumes:
      - sonarqube_conf:/opt/sonarqube/conf
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_bundled-plugins:/opt/sonarqube/lib/bundled-plugins
    networks:
      - sonarnet
    ports:
      - '9000:9000'
    environment:
      - sonar.jdbc.username=sonar
      - sonar.jdbc.password=sonar
      - sonar.jdbc.url=jdbc:postgresql://db:5432/sonar

  db:
    image: postgres
    networks:
      - sonarnet
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
    volumes:
      - postgresql:/var/lib/postgresql
      - postgresql_data:/var/lib/postgresql/data

networks:
  sonarnet:
    driver: bridge

volumes:
  sonarqube_conf:
  sonarqube_data:
  sonarqube_extensions:
  sonarqube_bundled-plugins:
  postgresql:
  postgresql_data:
  jenkins_data: