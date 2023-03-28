## Enable google API keys:
You should get and enable your API keys before run the code.  
Refer to the following steps.
<br>
<br>
### 1. Create project from Google Cloud Platform  
To create an API key, create project from following link,  
where example name of the project would be `capstoneproject`
- Goto  
https://console.cloud.google.com/projectselector2/apis/dashboard?supportedpurview=project
- 사용 설정된 API 및 서비스 > 프로젝트 만들기
- Create project with any name
<br>
<br>
### 2. API key request to developers:  
You should fill up the form before you can use this API.  
**Prior to this step is to create your project on:**  
https://console.cloud.google.com/

- Fill up the form from  
https://docs.google.com/forms/d/e/1FAIpQLSdhBBnVVVbXSElby-jhNnEj-Zwpt5toQSCFsJerGfpXW66CuQ/viewform?hl=ko  
    - __Contact Information__
        - Full Name : (Your name)
        - Organization Name : Seoul national university of science and technology
        - Organization Website : https://en.seoultech.ac.kr/
        - Organization country/region : South Korea  

    - __Project Information__  
        - Project Description : I would like to create an application which analyzes and summarizes given text input.
        - Languages : English, Korean
        - Google Cloud Project ID : **get from** https://console.cloud.google.com

    - __Contact Preferences__
        - Perspective API updates : (check optional)
        - Collaboration Opportunities : (check optional)
    
    - __Legal Information__
        - Consent Detail : (check mendatory)
- Wait for the confirmation:  
\<Reference>  
```Thanks for requesting access to Perspective API. We'll send you a confirmation email within an hour, and you will be able to view and enable the API in the Google Cloud Console. Until then, you can visit our website, perspectiveapi.com, to learn more about the API.```
<br>
<br>
### 3. Create your API key
- Goto  
https://console.cloud.google.com/projectselector2/apis/dashboard?supportedpurview=project
- 사용자 인증 정보 > 사용자 인증정보 만들기 > API 키
- Create key(It will be automatically generated.)
- [Warning!] Do not push your key on the github