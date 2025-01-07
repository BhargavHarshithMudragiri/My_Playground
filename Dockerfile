##Artifact Build Stage
FROM maven AS build_stage
RUN mkdir /opt/mywebapp
WORKDIR /opt/mywebapp
COPY . .
RUN mvn clean package ##artifact -- *.war

##Tomcat Deploy Stage
FROM tomcat
WORKDIR webapps
COPY --from=build_stage /opt/mywebapp/target/*.war .
RUN rm -rf ROOT && mv *.war ROOT.war
EXPOSE 8080
