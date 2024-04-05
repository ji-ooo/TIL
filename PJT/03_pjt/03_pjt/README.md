# PJT03
## 반응형 포트폴리오 웹사이트 구현

### 나를 소개하는 포트폴리오 사이트 구현하기
- HTML, CSS 파일 작성
- Bootstrap 내장 레이아웃, 콘텐츠 활용

> header
> -
> 배경 사진, 제목
> 
> 보이는 화면에 배경 꽉 차도록
>
> vh, vw 사용
> ```css
> .front-img {
>   background-image: url(./images/background.jpg);
>   background-repeat : no-repeat;
>   background-size: 100% 100%;
>   height: 100vh;
>   width: 100vw;
>   width: 100%;
>   text-align: center;
>   align-items: center;
>   color: white;
> }
> ```
>
> ---
> Navbar
> -
> sticky-top
> ```html
> <nav class="navbar sticky-top navbar-expand-lg" data-bs-theme="dark">
> ```
> width가 좁아지면 offcanvas형태로 nav 숨기기
> ```html
> <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
>   <span class="navbar-toggler-icon me-2"></span>
> </button>
> ```
>
> ---
> intro
> -
> 개발자를 꿈꾸게 된 계기
> 
> ---
> Skills
> -
> 적당한 이미지를 포함한 카드 형태
> 반응형으로 display: flex, wrap 되도록
> ```css
>.skills-container {
>   display: flex;
>   align-items: center;
>   justify-content: center;
>   flex-wrap: wrap;
>   padding: 2rem;
>   margin-bottom: 0;
> }
> ```
> 
> ---
> Project
> -
> 진행 했던 프로젝트들 게시
>
> ul - li
> 
> ---
> Contact
> -
> 집, 번호, 이메일, github 주소 게시
> 
> ```html
> <address class="address">
>   <div class="row ms-3">
>     <div class="col-12 col-md-6 col-xl-3">
>       <p class="address-title">&#x1F3E1 Address</p>
>       <p>울산광역시 동구 봉수로450</p>
>     </div>
>     <div class="col-12 col-md-6 col-xl-3">
>       <p class="address-title">&#x1F4DE Cell Phone</p>
>       <p>010-2533-5920</p>
>     </div>
>     <div class="col-12 col-md-6 col-xl-3">
>       <p class="address-title">&#x1F4E7 E-mail</p>
>       <p>andyandy0409@naver.com</p>
>     </div>
>     <div class="col-12 col-md-6 col-xl-3">
>       <p class="address-title">&#x1F680 Web site</p>
>       <p>https://github.com/ji-ooo</p>
>     </div>
>   </div>
> </address>
> ```
> row, col 활용하여 grid 배치
>
> &#x____ : 유니코드 이모지 
