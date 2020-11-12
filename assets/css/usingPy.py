s='''
@font-face {
  font-family: 'Monteserrat';
  src: url("../fonts/Montserrat-Regular.ttf"); }
@font-face {
  font-family: 'Monteserrat-Bold';
  src: url("../fonts/Montserrat-Bold.ttf"); }
@font-face {
  font-family: 'RobotoSlab-Bold';
  src: url("../fonts/RobotoSlab-Bold.ttf"); }
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box; }

html {
  scroll-behavior: smooth; }

body {
  font-family: 'Monteserrat', sans-serif;
  color: #1b262c; }

ul {
  list-style: none; }

a {
  text-decoration: none;
  color: black; }

header {
  position: sticky;
  top: 0;
  background-color: #3282b8;
  width: 100%;
  z-index: 1000;
  box-shadow: 3px 3px 30px 0 #1b262c; }

.container {
  position: relative;
  margin: 0 auto;
  display: flex;
  padding: 0.3rem 2rem;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox; }

.fixed-width {
  max-width: 1000px;
  margin: 0 auto; }

.logo-container {
  flex: 1;
  color: #1b262c;
  display: flex;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox; }
  .logo-container img {
    width: 60px;
    height: 60px;
    object-fit: cover;
    object-position: center;
    border-radius: 50%;
    margin-right: 5px; }
  .logo-container .logo {
    display: inline-block; }

.nav-btn {
  flex: 3;
  display: flex;
  height: 50px;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox; }

.nav-links {
  flex: 2; }

.log-sign {
  display: flex;
  justify-content: center;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center; }

#scrollUp {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #bbe1fa;
  color: #1b262c;
  display: flex;
  align-items: center;
  justify-content: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center;
  font-size: 2rem;
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  transition: .3s;
  z-index: 20000; }

#scrollUp:hover {
  color: #3282b8;
  bottom: 1.3rem; }

@keyframes jumping {
  from {
    bottom: 1rem; }
  to {
    bottom: 1.3rem; } }
header .logo {
  display: flex;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  text-transform: uppercase;
  line-height: 3rem;
  font-weight: 700;
  font-size: 1.8rem;
  color: #fff; }

header .logo span {
  font-weight: 300;
  margin-left: 5px; }

.btn {
  display: inline-block;
  color: white;
  padding: .5rem 1.2rem;
  border-radius: 2rem;
  border: 2px solid #fff;
  line-height: 1;
  margin: 0 .2rem;
  font-size: .8rem;
  text-transform: uppercase;
  transition: .3s;
  text-align: center; }

.btn.solid, .btn.transparent:hover {
  background: #fff;
  color: #69bde7; }

.btn.transparent, .btn.solid:hover {
  background: transparent;
  color: white; }

.nav-links > ul {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: flex-end;
  margin-right: 30px; }

.nav-link {
  position: relative; }

.nav-link > a {
  color: #fff;
  line-height: 2rem;
  padding: 0 .8rem;
  font-size: .95rem;
  letter-spacing: 1px;
  transition: .3s;
  display: flex;
  justify-content: space-between;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between; }

.nav-link > a > .svg-inline--fa.fa-w-10 {
  margin-left: .2rem; }

.nav-link:hover > a {
  transform: scale(1.1); }

.dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  width: 10rem;
  transform: translateY(10px);
  pointer-events: none;
  opacity: 0;
  transition: .3s; }

.dropdown-link:not(:nth-last-child(2)) {
  border-bottom: 1px solid #efefef; }

.dropdown-link ul {
  position: relative; }

.dropdown-link > a {
  background: #fff;
  display: flex;
  color: #3498db;
  padding: .5rem 1rem;
  font-size: .9rem;
  transition: .3s;
  align-items: center;
  justify-content: space-between;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between; }

.dropdown-link:hover > a {
  background: #3498db;
  color: #fff; }

.dropdown-link .svg-inline--fa.fa-w-10 {
  transform: rotate(-90deg); }

.arrow {
  position: absolute;
  width: 11px;
  height: 11px;
  top: -5.5px;
  left: 32px;
  background: #fff;
  transform: rotate(45deg);
  cursor: pointer;
  transition: .3s;
  z-index: -1; }

.dropdown-link:first-child:hover ~ .arrow {
  background: #3498db; }

.dropdown-link {
  position: relative; }

.dropdown.second {
  top: 0;
  left: 100%;
  padding-left: .8rem;
  cursor: pointer;
  transform: translateX(10px); }

.dropdown.second .arrow {
  top: 10px;
  left: -5.5px; }

.nav-link:hover > .dropdown,
.dropdown-link:hover > .dropdown {
  transform: translate(0, 0);
  pointer-events: auto;
  opacity: 1; }

.hamburger-menu-container {
  flex: 1;
  display: none;
  align-items: center;
  justify-content: flex-end;
  -ms-flex-align: center;
  -ms-flex-pack: flex-end; }

.hamburger-menu {
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center; }

.hamburger-menu div {
  width: 1.6rem;
  height: 3px;
  background-color: #fff;
  border-radius: 1rem;
  position: relative;
  z-index: 1001;
  transition: .3s; }

.hamburger-menu div::after,
.hamburger-menu div::before {
  content: '';
  width: inherit;
  height: inherit;
  border-radius: inherit;
  position: absolute;
  background-color: #fff;
  transition: .3s; }

.hamburger-menu div::before {
  transform: translateY(-7px); }

.hamburger-menu div::after {
  transform: translateY(7px); }

#check {
  position: absolute;
  top: 50%;
  width: 2.5rem;
  height: 2.5rem;
  transform: translateY(-50%);
  right: 2rem;
  z-index: 90000;
  cursor: pointer;
  opacity: 0;
  display: none; }

#check:checked ~ .hamburger-menu-container .hamburger-menu div {
  background-color: transparent; }

#check:checked ~ .hamburger-menu-container .hamburger-menu div::before {
  transform: translateY(0) rotate(-45deg); }

#check:checked ~ .hamburger-menu-container .hamburger-menu div::after {
  transform: translateY(0) rotate(45deg); }

#hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between;
  width: 100%;
  background: #1b262c;
  position: relative; }
  #hero .text {
    height: 100%;
    flex: 1;
    padding: 2rem 4rem; }
    #hero .text h1 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 4rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 400px;
      color: #3282b8; }
    #hero .text p {
      max-width: 320px;
      margin: 1rem 0;
      line-height: 2rem;
      font-size: 1rem;
      color: #bbe1fa; }
    #hero .text .cta {
      display: flex;
      justify-content: space-between;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: space-between;
      max-width: 330px;
      align-items: center;
      margin-top: 1.3rem; }
      #hero .text .cta .btn {
        transition: .3s;
        font-size: 1.3rem;
        border-color: #bbe1fa;
        color: #bbe1fa; }
      #hero .text .cta .btn:hover {
        transform: translateY(-2px);
        background: #3282b8;
        color: #1b262c;
        border-color: #3282b8; }
      #hero .text .cta .small {
        display: inline-block;
        color: #3282b8;
        margin-left: auto;
        transition: .3s; }
      #hero .text .cta .small:hover {
        transform: translateX(2px);
        color: #bbe1fa; }
  #hero .social-icons {
    display: none;
    justify-content: space-between;
    -ms-flex-pack: space-between;
    position: absolute;
    right: 2rem;
    bottom: 1rem;
    width: 250px; }
    #hero .social-icons li a {
      display: flex;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #1b262c;
      color: #bbe1fa;
      font-size: 1.5rem;
      transition: .3s; }
    #hero .social-icons li a:hover {
      transform: translateY(-2px);
      color: #1b262c;
      background: #bbe1fa; }
  #hero .image {
    background: url("../images/Young worker working in workshop.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 615px;
    flex: 1.5;
    clip-path: polygon(30% 0, 100% 0, 100% 100%, 0 100%);
    position: relative; }
    #hero .image .social-icons {
      display: flex;
      display: -ms-flexbox; }

#logos {
  display: flex;
  align-items: center;
  justify-content: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center;
  width: 100%;
  height: 100px;
  background: #bbe1fa;
  position: relative;
  padding: 5px 0; }
  #logos .slick-slider {
    margin-bottom: 0 !important; }
  #logos .logos {
    display: flex;
    position: relative;
    justify-content: space-around;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-around;
    height: 100%;
    width: 100%;
    padding: 5px 0; }
    #logos .logos .logo {
      width: 200px;
      height: 100px;
      background: #3282b8;
      margin: 5px 1px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: space-around; }
      #logos .logos .logo img {
        width: 80px;
        height: 80px;
        object-fit: cover;
        object-position: center;
        border-radius: 50%; }

.btn {
  font-weight: 900; }

#problems, #solutions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between;
  width: 100%;
  background: #0f4c75;
  padding: 10rem 2rem;
  flex-wrap: wrap; }
  #problems .text, #solutions .text {
    height: 100%;
    flex: 1; }
    #problems .text h2, #solutions .text h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 3rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 450px;
      color: #1b262c; }
    #problems .text p, #solutions .text p {
      max-width: 320px;
      margin: 1rem 0;
      line-height: 2rem;
      font-size: 1rem;
      color: #bbe1fa; }
    #problems .text .cta, #solutions .text .cta {
      display: flex;
      justify-content: space-between;
      max-width: 330px;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: space-between;
      margin-top: 1.3rem; }
      #problems .text .cta .btn, #solutions .text .cta .btn {
        transition: .3s;
        font-size: 1.3rem;
        border-color: #bbe1fa;
        color: #bbe1fa; }
      #problems .text .cta .btn:hover, #solutions .text .cta .btn:hover {
        transform: translateY(-2px);
        background: #3282b8;
        color: #1b262c;
        border-color: #3282b8; }
      #problems .text .cta .small, #solutions .text .cta .small {
        display: inline-block;
        color: #3282b8;
        margin-left: auto;
        transition: .3s; }
      #problems .text .cta .small:hover, #solutions .text .cta .small:hover {
        transform: translateX(2px);
        color: #bbe1fa; }
  #problems .list, #solutions .list {
    background: #fff;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: flex-end;
    padding: 1rem;
    padding-left: 3rem;
    clip-path: polygon(15% 0, 100% 0, 100% 100%, 15% 100%, 0% 50%);
    height: auto;
    max-width: 700px; }
    #problems .list ul, #solutions .list ul {
      list-style: none; }
      #problems .list ul li, #solutions .list ul li {
        display: flex;
        align-items: center;
        justify-content: start;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: start;
        padding: 0;
        margin: 1rem; }
        #problems .list ul li .icon, #solutions .list ul li .icon {
          display: block;
          font-size: 2rem;
          min-width: 60px;
          height: 60px;
          display: flex;
          justify-content: center;
          align-items: center;
          -ms-flex-align: center;
          display: -ms-flexbox;
          -ms-flex-pack: center;
          color: red;
          margin-right: 1rem; }
        #problems .list ul li p, #solutions .list ul li p {
          font-size: 1.1rem;
          font-weight: bold;
          color: #3282b8; }

#solutions {
  flex-direction: row-reverse;
  justify-content: space-between;
  -ms-flex-pack: space-between;
  background: #3282b8; }
  #solutions .text h2 {
    margin-left: auto;
    text-align: right; }
  #solutions .text p {
    margin-left: auto;
    text-align: right; }
  #solutions .text .cta {
    margin-left: auto; }
    #solutions .text .cta .btn:hover {
      background: #0f4c75;
      color: #bbe1fa; }
    #solutions .text .cta .small {
      color: #0f4c75; }
  #solutions .list {
    clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0% 100%);
    padding-left: 0;
    padding-right: 7rem; }
    #solutions .list ul li .icon {
      color: #4caf50; }

#benefits {
  padding: 4rem 2rem;
  background: #0f4c75; }
  #benefits .head {
    margin-bottom: 7rem; }
    #benefits .head h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 3rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 450px;
      color: #1b262c;
      position: relative; }
    #benefits .head h2::after {
      content: '';
      width: 30%;
      height: 4px;
      background: #3282b8;
      display: block;
      margin-right: auto;
      margin-top: 1rem; }
  #benefits .benefits {
    display: flex;
    justify-content: space-between;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-between;
    margin: 2rem 0 10rem 0;
    flex-wrap: wrap; }
    #benefits .benefits .text h3 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 2.4rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 450px;
      color: #1b262c; }
    #benefits .benefits .text p {
      max-width: 320px;
      margin: 1rem 0;
      line-height: 2rem;
      font-size: 1rem;
      color: #bbe1fa; }
    #benefits .benefits .text a {
      max-width: 320px;
      display: block;
      color: #3282b8;
      margin-right: auto;
      transition: .3s;
      text-decoration: underline;
      text-align: right;
      padding: 10px 0; }
    #benefits .benefits .text a:hover {
      transform: translateX(2px);
      color: #bbe1fa; }
  #benefits .benefits:nth-child(odd) {
    flex-direction: row-reverse; }

.imagex {
  display: flex;
  justify-content: center;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center;
  flex: 1; }
  .imagex .con {
    position: relative;
    max-width: 400px;
    height: 400px;
    transition: .3s; }
    .imagex .con img {
      position: relative;
      z-index: 4;
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 5px;
      transition: .3s; }
  .imagex .con:hover img {
    transform-origin: center;
    transform: scale(1.1); }
  .imagex .con:hover::before, .imagex .con:hover::after {
    content: '';
    background: #bbe1fa;
    opacity: 0.4; }
  .imagex .con::before, .imagex .con::after {
    content: '';
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: #3282b8;
    position: absolute;
    left: 100%;
    top: 0;
    z-index: 1;
    transform: translate3d(-70%, -30%, 0);
    transition: .3s; }
  .imagex .con::after {
    left: 0;
    top: 100%;
    z-index: 1;
    transform: translate3d(-30%, -70%, 0); }

.safety {
  background: #fff;
  padding: 8rem 0;
  position: relative;
  height: auto; }
  .safety .container {
    display: flex;
    justify-content: center;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: center;
    position: relative;
    z-index: 4; }
    .safety .container .text {
      padding: 4rem 2rem;
      background: #3282b8;
      max-width: 600px;
      height: 500px;
      position: relative; }
      .safety .container .text h2 {
        font-size: 4rem;
        font-family: 'RobotoSlab-Bold';
        text-align: center;
        color: #1b262c;
        text-transform: uppercase;
        max-width: 500px; }
      .safety .container .text .cta {
        margin: 0 auto;
        margin-top: 3rem;
        max-width: 350px; }
        .safety .container .text .cta .btn {
          font-size: 1.3rem;
          margin-right: 1rem; }
        .safety .container .text .cta .btn:hover {
          background: #0f4c75;
          color: #bbe1fa;
          border-color: #0f4c75; }
        .safety .container .text .cta .small {
          color: #0f4c75;
          transition: .3s;
          margin-left: 1rem; }
        .safety .container .text .cta .small:hover {
          transform: translateX(2px);
          color: #bbe1fa; }
    .safety .container .image {
      position: relative; }
      .safety .container .image img {
        width: 400px;
        height: 400px;
        object-fit: cover;
        object-position: center; }
      .safety .container .image .social-icons {
        display: flex;
        justify-content: space-between;
        position: absolute;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: space-between;
        right: 2rem;
        bottom: 1rem;
        width: 250px; }
        .safety .container .image .social-icons li a {
          display: flex;
          justify-content: center;
          align-items: center;
          -ms-flex-align: center;
          display: -ms-flexbox;
          -ms-flex-pack: center;
          width: 50px;
          height: 50px;
          border-radius: 50%;
          background: #1b262c;
          color: #bbe1fa;
          font-size: 1.5rem;
          transition: .3s; }
        .safety .container .image .social-icons li a:hover {
          transform: translateY(-2px);
          color: #1b262c;
          background: #bbe1fa; }
  .safety .design {
    width: 100%;
    height: 100%;
    background: #3282b8;
    opacity: .8;
    position: absolute;
    top: 0;
    right: 0;
    clip-path: polygon(60% 0, 100% 0, 100% 100%, 30% 100%); }

.services, .features, .faqs {
  padding: 4rem 2rem;
  background: #0f4c75; }
  .services .head, .features .head, .faqs .head {
    margin-bottom: 5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-between; }
    .services .head h2, .features .head h2, .faqs .head h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 3rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 450px;
      color: #3282b8;
      position: relative; }
    .services .head h2::after, .features .head h2::after, .faqs .head h2::after {
      content: '';
      width: 30%;
      height: 4px;
      background: #3282b8;
      display: block;
      margin-right: auto;
      margin-top: 1rem; }
    .services .head .quote, .features .head .quote, .faqs .head .quote {
      max-width: 400px;
      margin-right: 2rem; }
      .services .head .quote p, .features .head .quote p, .faqs .head .quote p {
        font-size: 1rem;
        line-height: 1.5rem;
        text-align: center;
        position: relative;
        z-index: 4;
        margin-bottom: 1rem;
        color: #bbe1fa; }
      .services .head .quote p::before, .services .head .quote p::after, .features .head .quote p::before, .features .head .quote p::after, .faqs .head .quote p::before, .faqs .head .quote p::after {
        content: '';
        width: 20px;
        height: 20px;
        background: #3282b8;
        position: absolute;
        z-index: -1;
        transition: .3s; }
      .services .head .quote p:hover::before, .services .head .quote p:hover::after, .features .head .quote p:hover::before, .features .head .quote p:hover::after, .faqs .head .quote p:hover::before, .faqs .head .quote p:hover::after {
        height: 10px;
        width: 100%; }
      .services .head .quote p:hover::after, .features .head .quote p:hover::after, .faqs .head .quote p:hover::after {
        right: 0rem; }
      .services .head .quote p:hover::before, .features .head .quote p:hover::before, .faqs .head .quote p:hover::before {
        left: 0rem; }
      .services .head .quote p::before, .features .head .quote p::before, .faqs .head .quote p::before {
        left: -1.5rem;
        top: -1rem; }
      .services .head .quote p::after, .features .head .quote p::after, .faqs .head .quote p::after {
        bottom: -1rem;
        right: -1.5rem; }
      .services .head .quote span, .features .head .quote span, .faqs .head .quote span {
        display: block;
        text-align: right;
        font-weight: bold;
        font-size: .9rem;
        margin: 1rem 1rem 0 0;
        color: #bbe1fa; }
  .services .contents, .features .contents, .faqs .contents {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    -ms-flex-align: flex-start;
    display: -ms-flexbox;
    -ms-flex-pack: space-around;
    flex-wrap: wrap; }
    .services .contents .card, .features .contents .card, .faqs .contents .card {
      padding: 1rem;
      text-align: center;
      border-radius: 5px;
      background: #1b262c;
      width: 325px;
      margin: 2rem 10px; }
      .services .contents .card h3, .features .contents .card h3, .faqs .contents .card h3 {
        text-transform: uppercase;
        color: #3282b8;
        margin: 2rem 0;
        font-family: 'Monteserrat-Bold';
        font-size: 1.6rem; }
      .services .contents .card .cta, .features .contents .card .cta, .faqs .contents .card .cta {
        margin: 2rem 0; }
        .services .contents .card .cta .btn, .features .contents .card .cta .btn, .faqs .contents .card .cta .btn {
          border-radius: 5px;
          border-color: #3282b8;
          color: #3282b8; }
        .services .contents .card .cta .btn:hover, .features .contents .card .cta .btn:hover, .faqs .contents .card .cta .btn:hover {
          background: #3282b8;
          color: #fff; }
        .services .contents .card .cta .small, .features .contents .card .cta .small, .faqs .contents .card .cta .small {
          color: #eee;
          transition: .3s;
          display: inline-block;
          font-size: 0.8rem;
          text-decoration: underline; }
        .services .contents .card .cta .small:hover, .features .contents .card .cta .small:hover, .faqs .contents .card .cta .small:hover {
          color: #fff;
          transform: translateX(2px); }
      .services .contents .card p, .features .contents .card p, .faqs .contents .card p {
        color: #bbe1fa;
        margin: 1rem;
        font-size: 1rem;
        line-height: 1.5rem; }

.features, .faqs {
  background: #3282b8; }
  .features .head h2, .faqs .head h2 {
    color: #1b262c; }
  .features .head h2::after, .faqs .head h2::after {
    background: #0f4c75; }
  .features .head .quote p::before, .features .head .quote p::after, .faqs .head .quote p::before, .faqs .head .quote p::after {
    background: #bbe1fa; }
  .features .contents .card, .faqs .contents .card {
    width: 350px;
    height: 350px;
    border-radius: 48%;
    position: relative;
    padding: 2rem 3rem; }
    .features .contents .card h3, .faqs .contents .card h3 {
      margin-top: 4rem; }
      .features .contents .card h3 a, .faqs .contents .card h3 a {
        color: #3282b8; }
    .features .contents .card .icon, .faqs .contents .card .icon {
      display: flex;
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: #bbe1fa;
      color: #3282b8;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      margin: 0 auto;
      font-size: 3rem;
      position: absolute;
      top: 0;
      left: 50%;
      transform: translate3d(-50%, -50%, 0); }

#reviews .cta {
  max-width: 400px;
  margin-top: 3rem;
  margin-left: auto;
  display: flex;
  align-items: center;
  justify-content: space-around;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  flex-wrap: wrap; }
  #reviews .cta .btn {
    font-size: 1.4rem;
    margin-right: 2rem; }
  #reviews .cta .btn:hover {
    background: #3282b8;
    color: #fff;
    border-color: #3282b8; }
  #reviews .cta .small {
    color: #bbe1fa;
    display: inline-block;
    transition: .3s; }
  #reviews .cta .small:hover {
    transform: translateX(2px);
    color: #3282b8; }
#reviews .contents .card small {
  color: #3282b8;
  display: block;
  margin: 1rem auto; }

#newsletter {
  background: url(../images/about.jpg); }
  #newsletter .letter {
    padding: 6rem 4rem;
    background: rgba(27, 38, 44, 0.93);
    text-align: center; }
    #newsletter .letter h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 4rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 600px;
      color: #3282b8;
      position: relative;
      margin: 0 auto; }
    #newsletter .letter p {
      color: #bbe1fa;
      font-size: 1rem;
      line-height: 1.5rem;
      max-width: 400px;
      margin: 1rem auto;
      margin-bottom: 3rem; }
    #newsletter .letter form {
      margin: 2rem 0; }
      #newsletter .letter form .email {
        position: relative;
        max-width: 400px;
        margin: 2rem auto;
        background: #fff;
        border-radius: 5px; }
        #newsletter .letter form .email label {
          font-weight: 900;
          font-size: 1.1rem;
          color: #3282b8;
          position: absolute;
          left: 0;
          top: -1.7rem; }
        #newsletter .letter form .email input {
          font-size: 1.2rem;
          padding: 10px 15px;
          border: none;
          outline: none;
          width: 100%;
          font-family: 'Monteserrat';
          border-radius: 5px; }
        #newsletter .letter form .email .bottom {
          width: 100%;
          height: 5px;
          background: #3282b8;
          border-radius: 0 0 5px 5px; }
      #newsletter .letter form button {
        padding: 10px 20px;
        border-radius: 7px;
        font-weight: 900;
        background: transparent;
        border: 2px solid #3282b8;
        color: #3282b8;
        font-family: 'Monteserrat';
        cursor: pointer;
        margin-top: -1rem;
        transition: .3s; }
      #newsletter .letter form button:hover {
        background: #3282b8;
        color: #fff; }

.faqs .search form {
  margin: 2rem 0; }
  .faqs .search form .group {
    position: relative;
    max-width: 400px;
    margin: 2rem auto;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: center; }
    .faqs .search form .group label {
      font-weight: 900;
      font-size: 1.3rem;
      color: #1b262c;
      position: absolute;
      left: 0;
      top: -1.5rem; }
    .faqs .search form .group input {
      font-size: 1.2rem;
      padding: 10px 15px;
      border: none;
      outline: none;
      width: 100%;
      font-family: 'Monteserrat';
      border-radius: 5px;
      flex: 1;
      height: 38px; }
    .faqs .search form .group button {
      display: flex;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      width: 50px;
      height: 50px;
      font-size: 1.4rem;
      background: #bbe1fa;
      color: #1b262c;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      transition: .3s;
      margin-left: 10px; }
    .faqs .search form .group button:hover {
      background: #1b262c;
      color: #fff; }
.faqs .contents .card {
  padding: 0;
  border-radius: 0;
  height: auto; }
  .faqs .contents .card .q, .faqs .contents .card .a {
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: center;
    background: #fff; }
    .faqs .contents .card .q span, .faqs .contents .card .a span {
      display: block;
      font-size: 2rem;
      color: #1b262c;
      font-weight: bolder; }
    .faqs .contents .card .q p, .faqs .contents .card .a p {
      margin: 0;
      text-align: right;
      color: #3282b8; }
  .faqs .contents .card .a {
    background: #1b262c; }
    .faqs .contents .card .a span {
      color: #fff; }
    .faqs .contents .card .a p {
      color: #3282b8; }
.faqs .cta {
  max-width: 400px;
  margin-top: 3rem;
  margin-left: auto;
  display: flex;
  align-items: center;
  justify-content: space-around;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  flex-wrap: wrap; }
  .faqs .cta .btn {
    font-size: 1.4rem;
    margin-right: 2rem; }
  .faqs .cta .btn:hover {
    background: #0f4c75;
    color: #fff;
    border-color: #0f4c75; }
  .faqs .cta .small {
    color: #bbe1fa;
    display: inline-block;
    transition: .3s; }
  .faqs .cta .small:hover {
    transform: translateX(2px);
    color: #1b262c; }

#contact .contents {
  justify-content: space-around;
  -ms-flex-pack: space-around; }
  #contact .contents .social .link {
    display: flex;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    margin: 2rem 0; }
    #contact .contents .social .link .icon {
      display: flex;
      min-width: 60px;
      height: 60px;
      border-radius: 50%;
      background: #bbe1fa;
      color: #3282b8;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      font-size: 1.8rem; }
    #contact .contents .social .link .text {
      margin-left: 1rem; }
      #contact .contents .social .link .text a {
        font-size: 1.3rem;
        color: #bbe1fa; }
      #contact .contents .social .link .text p {
        font-size: 1.3rem;
        color: #bbe1fa; }
      #contact .contents .social .link .text h3 {
        text-transform: uppercase;
        font-size: .9rem;
        font-family: 'Monteserrat-Bold'; }

.direct {
  background: #1b262c;
  max-width: 350px;
  padding: 1rem;
  border-radius: 4px; }
  .direct form legend {
    font-family: 'Monteserrat-Bold';
    font-size: 1.6rem;
    color: #3282b8;
    text-transform: uppercase;
    margin: 1rem 0; }
  .direct form .btn {
    background: #3282b8;
    color: #bbe1fa;
    border: none;
    font-family: 'Monteserrat-Bold';
    margin: 1rem auto;
    font-weight: 900;
    padding: 14px 1rem;
    opacity: .8;
    display: flex;
    justify-content: space-around;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-around;
    cursor: pointer; }
    .direct form .btn .send {
      display: block;
      margin-right: 10px;
      font-size: 1.3rem;
      transition: inherit; }
    .direct form .btn span {
      display: block;
      font-size: 1.1rem; }
  .direct form .btn:hover {
    transform: translateY(-2px);
    opacity: 1; }
    .direct form .btn:hover .send {
      transform-origin: center;
      transform: scale(1.1); }
  .direct form .input {
    position: relative;
    margin: 3rem 0;
    border-radius: 4px;
    background: #fff; }
    .direct form .input label {
      position: absolute;
      left: 15px;
      color: #1b262c;
      top: 10px;
      transition: .3s; }
    .direct form .input input, .direct form .input textarea {
      width: 100% !important;
      padding: 10px 15px;
      font-family: 'Monteserrat';
      font-size: 1rem;
      border: none;
      outline: none;
      border-radius: 4px;
      margin: 0;
      position: relative;
      z-index: 4;
      background: transparent; }
    .direct form .input .bottom {
      position: absolute;
      width: 0;
      height: 4px;
      left: 0;
      bottom: -4px;
      background: #3282b8;
      border-radius: 0 0 4px 4px;
      transition: .3s;
      margin: 0 auto; }
    .direct form .input small {
      position: absolute;
      right: 0;
      bottom: -1.4rem;
      color: #bbe1fa;
      font-style: italic; }
  .direct form .input.active {
    border-radius: 4px 4px 0 0; }
    .direct form .input.active label {
      top: -1.5rem;
      left: 0;
      color: #3282b8; }
    .direct form .input.active .bottom {
      opacity: 1;
      width: 100%; }
    .direct form .input.active input {
      border-radius: 4px 4px 0 0; }
  .direct form .input:nth-child(2) {
    margin-top: 2rem; }
  .direct form .input.radio, .direct form .input.file {
    background: transparent; }
    .direct form .input.radio label, .direct form .input.file label {
      position: static;
      color: #fff; }
    .direct form .input.radio ul, .direct form .input.file ul {
      list-style: none;
      margin-top: 1rem; }
      .direct form .input.radio ul li, .direct form .input.file ul li {
        display: inline-block;
        margin: 5px 10px; }
        .direct form .input.radio ul li input, .direct form .input.file ul li input {
          color: #fff;
          width: auto !important;
          cursor: pointer; }
        .direct form .input.radio ul li label, .direct form .input.file ul li label {
          margin-left: 5px;
          cursor: pointer; }
  .direct form .input.file {
    margin-top: 3.6rem; }
    .direct form .input.file label {
      margin-bottom: 0.6rem;
      display: inline-block; }
    .direct form .input.file input {
      margin: .3rem 0;
      color: #fff; }

.direct.error form .input small {
  color: red; }

#new, #keyword, #referral, #other {
  display: none; }

#footer {
  background: #1b262c;
  display: flex;
  flex-wrap: wrap;
  display: -ms-flexbox;
  padding: 1rem; }
  #footer .links {
    width: 400px;
    margin: 1rem; }
    #footer .links legend {
      color: #3282b8;
      font-weight: 900;
      text-transform: uppercase;
      font-size: 1.4rem;
      margin: 1rem 0; }
    #footer .links ul {
      padding-left: 10px; }
      #footer .links ul li {
        margin: .8rem 0;
        transition: .3s;
        cursor: pointer; }
        #footer .links ul li a {
          color: #fff;
          transition: .3s;
          font-weight: lighter; }
      #footer .links ul li:hover {
        transform: translateX(4px); }
        #footer .links ul li:hover a {
          color: #bbe1fa; }
    #footer .links .locations {
      padding: 0;
      display: flex;
      display: -ms-flexbox;
      flex-wrap: wrap; }
      #footer .links .locations li {
        text-align: center;
        margin: 1rem 0.8rem;
        padding: 1rem; }
        #footer .links .locations li span {
          display: flex;
          justify-content: center;
          align-items: center;
          -ms-flex-align: center;
          display: -ms-flexbox;
          -ms-flex-pack: center;
          width: 60px;
          margin: .5rem auto;
          height: 60px;
          background: #3282b8;
          border-radius: 50%;
          color: #fff;
          font-size: 2rem; }
        #footer .links .locations li p {
          color: #3282b8; }
      #footer .links .locations li:hover {
        transform: none;
        background: #fff; }
    #footer .links .about {
      width: 100%; }
      #footer .links .about img {
        width: 200px;
        height: 200px;
        border-radius: 5px;
        object-fit: cover; }
      #footer .links .about p {
        color: #bbe1fa;
        font-size: 1rem;
        line-height: 1.6rem;
        margin: 1rem 0; }
      #footer .links .about a {
        color: #1b262c;
        transition: .3s;
        display: inline-block;
        background: #3282b8;
        padding: 8px 12px;
        border-radius: 5px; }
      #footer .links .about a:hover {
        color: #fff;
        transform: translateX(3px); }

#credit {
  width: 100%;
  padding: 1rem;
  background: #0f4c75;
  text-align: center; }
  #credit p {
    color: #fff;
    line-height: 1.4rem; }
  #credit a {
    transition: .3s;
    font-weight: bolder;
    display: inline-block;
    transform-origin: left; }
  #credit a:hover {
    transform: scale(1.1);
    color: #bbe1fa; }

.subhero {
  background: url("../images/contact_hero.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  clip-path: polygon(0 0, 100% 0, 100% 90%, 55% 90%, 50% 100%, 45% 90%, 0 90%);
  background-position: center; }
  .subhero .overlay {
    padding: 10rem 4rem;
    display: flex;
    justify-content: center;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: center;
    background: rgba(27, 38, 44, 0.7);
    position: relative; }
    .subhero .overlay h1 {
      text-align: center;
      font-size: 4rem;
      text-transform: uppercase;
      font-family: 'RobotoSlab-Bold';
      color: #3282b8; }
    .subhero .overlay p {
      color: #fff;
      position: absolute;
      bottom: 6rem; }
  .subhero .overlay.blog_mode h1 {
    margin-bottom: 5rem; }
  .subhero .overlay.blog_mode .info {
    position: absolute;
    bottom: 4rem;
    display: flex;
    min-width: 300px;
    align-items: center;
    justify-content: space-between;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-between; }
    .subhero .overlay.blog_mode .info li {
      display: flex;
      align-items: center;
      justify-content: space-between;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: space-between;
      margin: 10px 1.2rem; }
      .subhero .overlay.blog_mode .info li span {
        display: flex;
        width: 40px;
        height: 40px;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        border-radius: 50%;
        background: #fff;
        color: #3282b8;
        transition: .3s; }
      .subhero .overlay.blog_mode .info li span:hover {
        transform: scale(1.1); }
      .subhero .overlay.blog_mode .info li p {
        margin-left: 10px;
        position: static; }
    .subhero .overlay.blog_mode .info li.like span {
      cursor: pointer; }
    .subhero .overlay.blog_mode .info li.like span:hover {
      color: tomato; }
  .subhero .overlay.blog_mode .one {
    left: 1rem; }
  .subhero .overlay.blog_mode .two {
    right: 1rem; }

.project {
  padding: 6rem 1rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-around; }
  .project .text {
    max-width: 400px; }
    .project .text h2 {
      font-size: 3rem;
      text-transform: uppercase;
      color: #1b262c;
      margin-bottom: 1.3rem; }
    .project .text p {
      font-size: 1.1rem;
      line-height: 1.5rem; }
  .project .imagex {
    max-width: 400px; }

.company {
  padding: 6rem 1rem;
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  -ms-flex-align: flex-start;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  flex-wrap: wrap; }
  .company .image img {
    width: 300px;
    height: 300px;
    object-fit: cover;
    object-position: center;
    border-radius: 5px; }
  .company .details {
    max-width: 500px; }
    .company .details .data {
      margin: 1rem 0;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      -ms-flex-align: flex-start;
      display: -ms-flexbox;
      -ms-flex-pack: space-between; }
      .company .details .data .key {
        color: #3282b8;
        font-weight: bold;
        font-size: 1.2rem;
        width: 130px;
        position: relative;
        transition: .3s; }
      .company .details .data .key::before {
        content: '';
        width: 10px;
        height: 10px;
        background: #3282b8;
        transform: rotate(45deg) translateY(-50%);
        position: absolute;
        left: -35px;
        top: 50%;
        transition: .3s; }
      .company .details .data .value {
        flex: 1;
        font-size: 1rem;
        line-height: 1.4rem; }
    .company .details .data:hover .key::before {
      width: 20px;
      height: 20px;
      background: #0f4c75;
      transform: rotate(360deg) translateY(-50%);
      border-radius: 50%; }
    .company .details .data:hover .key {
      color: #0f4c75; }

.scores {
  display: flex;
  justify-content: space-around;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  padding: 4rem 1rem;
  flex-wrap: wrap; }
  .scores .score {
    text-align: center;
    position: relative;
    padding: 1rem 2rem;
    transition: .3s;
    margin: 1rem 10px;
    z-index: 2; }
    .scores .score .icon {
      display: flex;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: #3282b8;
      font-size: 4rem;
      color: #fff;
      margin: 1rem auto;
      position: relative;
      z-index: 2; }
    .scores .score h4 {
      text-transform: uppercase;
      font-size: 1.3rem;
      margin: 0.5rem 0;
      position: relative;
      z-index: 2;
      color: #1b262c;
      transition: .3s; }
    .scores .score h2 {
      font-family: 'RobotoSlab-Bold';
      font-size: 3rem;
      position: relative;
      z-index: 2;
      color: #1b262c;
      transition: .3s; }
  .scores .score::before {
    content: '';
    width: 100%;
    height: 5px;
    background: #0f4c75;
    position: absolute;
    left: 0;
    top: 0;
    transition: .3s;
    display: block;
    z-index: 1; }
  .scores .score:hover::before {
    height: 100%; }
  .scores .score:hover h2 {
    color: #fff; }
  .scores .score:hover h4 {
    color: #fff; }

.gallery {
  padding: 5rem 1rem;
  background: #1b262c;
  text-align: center; }
  .gallery h2 {
    font-family: 'RobotoSlab-Bold';
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 3rem;
    color: #3282b8; }
  .gallery .contents {
    margin: 1rem auto;
    display: flex;
    justify-content: space-around;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-around;
    flex-wrap: wrap; }
    .gallery .contents img {
      width: 200px;
      height: 300px;
      object-fit: cover;
      object-position: center;
      border-radius: 5px;
      margin: 1rem 10px; }

.contactPage {
  background: #0f4c75; }

.faqPage {
  background: #3282b8; }

.map {
  background: #fff;
  padding: 5rem 1rem; }
  .map h2 {
    font-size: 3rem;
    font-family: 'RobotoSlab-Bold';
    margin-bottom: 2rem; }
  .map .maps {
    display: flex;
    justify-content: space-around;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: space-around;
    flex-wrap: wrap; }
    .map .maps .gmap {
      margin: 0 1rem;
      flex: 1;
      flex-basis: 300px; }
      .map .maps .gmap h4 {
        text-transform: uppercase;
        font-weight: bold;
        margin: 0.5rem 0; }
      .map .maps .gmap .mapx {
        height: 300px;
        background: #3282b8; }

.ask {
  padding: 12rem 1rem 6rem 1rem;
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  -ms-flex-align: flex-start;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  background: #fff;
  clip-path: polygon(0 0, 50% 6rem, 100% 0, 100% 100%, 0 100%);
  flex-wrap: wrap; }
  .ask .text {
    flex-basis: 400px;
    margin: 1rem 10px; }
    .ask .text h2 {
      font-family: 'RobotoSlab-Bold';
      font-size: 3.4rem;
      margin: 1rem 0;
      text-transform: uppercase; }
    .ask .text p {
      line-height: 1.5rem;
      font-size: 1rem; }
  .ask .direct {
    margin: 1rem 10px; }

.history {
  display: flex;
  justify-content: space-around;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-around;
  padding: 5rem 1rem;
  flex-wrap: wrap; }
  .history .text {
    flex-basis: 600px;
    margin: 1rem 1rem; }
    .history .text h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 3rem;
      font-family: 'RobotoSlab-Bold';
      color: #3282b8;
      position: relative;
      margin-bottom: 2rem;
      max-width: 400px; }
    .history .text h2::after {
      content: '';
      width: 30%;
      height: 4px;
      background: #3282b8;
      display: block;
      margin-right: auto;
      margin-top: 1rem; }
    .history .text p {
      font-size: 1rem;
      line-height: 1.5rem;
      margin: 1rem 0; }
  .history .side {
    margin: 1rem 1rem;
    flex-basis: 500px;
    position: relative;
    cursor: move; }
    .history .side span {
      display: flex;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      font-size: 30rem;
      color: #3282b8;
      transition: .3s;
      filter: grayscale(1); }
    .history .side .tiny {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      object-fit: cover;
      object-position: center;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate3d(-100%, -100%, 0);
      transform-origin: center;
      transition: .3s;
      filter: grayscale(1) blur(2px); }
  .history .side:hover .tiny {
    transform: scale(1.5) translate3d(-65%, -65%, 0);
    filter: grayscale(0); }
  .history .side:hover span {
    color: #0f4c75;
    filter: grayscale(0); }

.ethos {
  padding: 6rem 1rem;
  text-align: center;
  background: #1b262c; }
  .ethos h2 {
    text-transform: uppercase;
    font-weight: bolder;
    font-size: 3rem;
    font-family: 'RobotoSlab-Bold';
    color: #3282b8;
    position: relative; }
  .ethos h2::before {
    content: '';
    width: 7rem;
    height: 4px;
    background: #3282b8;
    display: block;
    margin: 0.5rem auto; }
  .ethos p {
    line-height: 1.8rem;
    font-size: 1.1rem;
    font-weight: bold;
    color: #fff;
    max-width: 450px;
    margin: 1rem auto; }
  .ethos .btn {
    margin: 1rem 0 0 0;
    font-size: 1.5rem; }
  .ethos .btn:hover {
    background: #0f4c75;
    border-color: #0f4c75; }

.structure {
  padding: 3rem 1rem;
  text-align: center;
  background: #bbe1fa; }
  .structure h2 {
    text-transform: uppercase;
    font-weight: bolder;
    font-size: 3rem;
    font-family: 'RobotoSlab-Bold';
    color: #1b262c;
    position: relative; }
  .structure h2::before {
    content: '';
    width: 7rem;
    height: 4px;
    background: #1b262c;
    display: block;
    margin: 0.5rem auto; }
  .structure .box {
    max-width: 600px;
    height: 600px;
    margin: 3rem auto;
    position: relative; }
    .structure .box .circle {
      width: 160px;
      height: 160px;
      border-radius: 50%;
      background: #0f4c75;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      position: absolute;
      transition: .3s;
      cursor: cell;
      transform-origin: center; }
    .structure .box .mechanical {
      left: 50%;
      transform: translate3d(-50%, 0, 0);
      top: 0; }
    .structure .box .maintenance {
      top: 50%;
      transform: translate3d(0, -50%, 0);
      left: 0; }
    .structure .box .nimrod {
      top: 50%;
      transform: translate3d(-50%, -50%, 0);
      left: 50%; }
    .structure .box .customer {
      left: 50%;
      transform: translate3d(-50%, 0, 0);
      bottom: 0; }
    .structure .box .works {
      top: 50%;
      transform: translate3d(0, -50%, 0);
      right: 0; }
    .structure .box .circle:hover {
      background: #3282b8; }

.learnmore .side span {
  color: #3282b8;
  filter: grayscale(0); }
.learnmore .side .tiny {
  filter: grayscale(0.8); }

.learnmore.two {
  flex-direction: row-reverse; }
  .learnmore.two .text {
    text-align: right; }
    .learnmore.two .text h2 {
      margin-left: auto; }
    .learnmore.two .text h2::after {
      margin-left: auto;
      margin-right: 0; }

.allservices {
  padding: 12rem 1rem 6rem 1rem;
  clip-path: polygon(0 0, 50% 6rem, 100% 0, 100% 100%, 0 100%);
  background: #bbe1fa; }
  .allservices .head {
    margin-bottom: 5rem; }
    .allservices .head h2 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 3rem;
      font-family: 'RobotoSlab-Bold';
      max-width: 450px;
      color: #3282b8;
      position: relative; }
    .allservices .head h2::after {
      content: '';
      width: 30%;
      height: 4px;
      background: #3282b8;
      display: block;
      margin-right: auto;
      margin-top: 1rem; }
  .allservices .contents {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: flex-start;
    flex-wrap: wrap; }
    .allservices .contents li {
      min-width: 200px;
      padding: 1rem 1.3rem;
      margin: .4rem 10px;
      position: relative;
      cursor: pointer;
      background: #fff; }
      .allservices .contents li a {
        position: relative;
        z-index: 3;
        transition: .3s; }
    .allservices .contents li::after {
      content: '';
      position: absolute;
      width: 3px;
      height: 100%;
      left: 0;
      top: 0;
      background: #0f4c75;
      z-index: 1;
      transition: .1s; }
    .allservices .contents li:hover::after {
      width: 100%;
      transition: .3s; }
    .allservices .contents li:hover a {
      color: #fff; }

#quote-form {
  padding: 6rem 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: center; }
  #quote-form .form-parent {
    max-width: 350px; }
    #quote-form .form-parent .position {
      margin: 2rem 0;
      display: flex;
      align-items: center;
      justify-content: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: center;
      min-height: 60px; }
      #quote-form .form-parent .position span {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        border-radius: 50%;
        background: #0f4c75;
        color: #fff;
        margin: 0 .4rem;
        transition: .3s; }
      #quote-form .form-parent .position span.active {
        width: 60px;
        height: 60px;
        background: #4caf50;
        color: #fff;
        font-size: 1.7rem;
        font-weight: bold; }
    #quote-form .form-parent .form-container .direct {
      display: none; }
    #quote-form .form-parent .form-container .direct.active {
      display: block; }
    #quote-form .form-parent .form-container .direct.final {
      color: #fff;
      text-align: center; }
      #quote-form .form-parent .form-container .direct.final h3 {
        font-family: 'RobotoSlab-Bold';
        margin: 2rem 0;
        max-width: 300px;
        font-size: 1.5rem; }
        #quote-form .form-parent .form-container .direct.final h3 span {
          width: 40px;
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          -ms-flex-align: center;
          display: -ms-flexbox;
          -ms-flex-pack: center;
          border-radius: 50%;
          background: #0f4c75;
          margin: .2rem auto; }
      #quote-form .form-parent .form-container .direct.final p {
        line-height: 1.6rem;
        margin: 0 0 1.5rem 0; }
      #quote-form .form-parent .form-container .direct.final .btn {
        margin: 0 0 2rem 0; }
      #quote-form .form-parent .form-container .direct.final .btn:hover {
        background: #0f4c75;
        border-color: #0f4c75; }

.blog-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between;
  padding: 3rem 1rem 4rem 1rem;
  flex-wrap: wrap; }
  .blog-head h2 {
    text-transform: uppercase;
    font-weight: bolder;
    font-size: 3rem;
    font-family: 'RobotoSlab-Bold';
    color: #3282b8;
    position: relative;
    max-width: 400px; }
  .blog-head h2::after {
    content: '';
    width: 30%;
    height: 4px;
    background: #3282b8;
    display: block;
    margin-right: auto;
    margin-top: .2rem; }
  .blog-head .blog-search {
    background: transparent;
    padding: 0;
    flex: 1;
    margin: 0;
    max-width: 500px; }
    .blog-head .blog-search form {
      display: flex;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox; }
      .blog-head .blog-search form .input {
        flex: 1;
        background: #bbe1fa;
        margin: 0; }
        .blog-head .blog-search form .input small {
          display: none;
          color: red; }
      .blog-head .blog-search form button {
        background: transparent;
        border: none;
        outline: none;
        margin-left: .7rem; }
        .blog-head .blog-search form button span {
          display: flex;
          justify-content: center;
          align-items: center;
          -ms-flex-align: center;
          display: -ms-flexbox;
          -ms-flex-pack: center;
          width: 50px;
          height: 50px;
          border-radius: 50%;
          background: #3282b8;
          color: #fff;
          font-size: 1.5rem;
          font-weight: bold;
          cursor: pointer;
          transition: .3s; }
        .blog-head .blog-search form button span:hover {
          background: #1b262c;
          color: #3282b8;
          transform: scale(1.1) rotate(90deg); }

.main-blog {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  -ms-flex-align: center;
  display: -ms-flexbox;
  -ms-flex-pack: space-between;
  flex-wrap: wrap;
  padding: 0 1rem 2rem 1rem; }
  .main-blog .posts {
    max-width: 400px;
    margin: 10px 1rem; }
    .main-blog .posts .result {
      font-size: 1.7rem;
      font-weight: bolder;
      margin-bottom: 1.3rem;
      border-bottom: 3px solid #3282b8;
      padding-bottom: .4rem; }
    .main-blog .posts .contents .card {
      background: rgba(0, 33, 51, 0.07);
      border-radius: 5px;
      padding: 1rem;
      position: relative;
      margin: 1rem 0;
      max-width: 350px; }
      .main-blog .posts .contents .card .h {
        font-family: 'RobotoSlab-Bold';
        font-size: 1.7rem;
        text-transform: uppercase;
        color: #0f4c75;
        position: relative;
        z-index: 3; }
      .main-blog .posts .contents .card .cartegory {
        display: block;
        margin-bottom: 1rem;
        font-weight: bold;
        font-size: .9rem;
        position: relative;
        z-index: 3; }
      .main-blog .posts .contents .card p {
        line-height: 1.5rem;
        position: relative;
        z-index: 3; }
      .main-blog .posts .contents .card .by {
        display: block;
        text-align: right;
        margin: 1rem 0 0 0;
        position: relative;
        z-index: 3; }
      .main-blog .posts .contents .card .circle {
        position: absolute;
        width: 100%;
        height: 100%;
        background: #bbe1fa;
        right: 0;
        bottom: 0;
        z-index: 1;
        border-radius: 5px;
        transition: .1s;
        clip-path: circle(0px at right bottom); }
    .main-blog .posts .contents .card:hover .circle {
      transition: .5s; }
  .main-blog .sidebar {
    max-width: 300px;
    margin: 10px 1rem; }
    .main-blog .sidebar .card {
      margin: 1rem 0; }
      .main-blog .sidebar .card .head {
        padding: 5px 15px;
        font-size: 1.4rem;
        font-family: 'RobotoSlab-Bold';
        background: #0f4c75;
        color: #fff;
        clip-path: polygon(0 0, 70% 0, 80% 100%, 0 100%); }
      .main-blog .sidebar .card ul {
        padding: 1px .7rem;
        background: #3282b8; }
        .main-blog .sidebar .card ul li {
          margin: 14px 0; }
          .main-blog .sidebar .card ul li a {
            color: #bbe1fa;
            transition: .3s; }
          .main-blog .sidebar .card ul li a:hover {
            color: #fff;
            margin-left: 3px; }
      .main-blog .sidebar .card .socialFrame {
        height: 150px;
        background: #3282b8;
        position: relative; }
        .main-blog .sidebar .card .socialFrame .btn {
          position: absolute;
          left: 50%;
          transform: translate3d(-50%, 0, 0);
          bottom: 1rem; }
        .main-blog .sidebar .card .socialFrame .btn:hover {
          background: #fff;
          color: #3282b8; }
      .main-blog .sidebar .card .newslett {
        border-radius: 0; }
  .main-blog .post_detail {
    margin: 2rem 0; }
    .main-blog .post_detail .image {
      text-align: center; }
      .main-blog .post_detail .image img {
        object-fit: cover;
        width: 100%;
        height: 500px;
        display: block; }
      .main-blog .post_detail .image span {
        margin: 10px 0;
        font-weight: bold;
        font-size: 1rem;
        line-height: 1.5rem;
        display: block; }
    .main-blog .post_detail .content {
      margin: 1rem 0;
      max-width: 700px; }
      .main-blog .post_detail .content h2 {
        font-family: 'RobotoSlab-bold';
        font-size: 2rem;
        margin-bottom: 1.3rem;
        position: relative;
        display: inline-block; }
      .main-blog .post_detail .content h2::after {
        content: '';
        width: 50%;
        height: 5px;
        background: #0f4c75;
        display: block;
        margin-top: 5px; }
      .main-blog .post_detail .content p {
        font-size: 1rem;
        line-height: 1.6rem; }
      .main-blog .post_detail .content ul {
        margin: 1rem 0;
        list-style: disc; }
        .main-blog .post_detail .content ul legend {
          font-size: 1.5rem;
          font-weight: bold;
          margin-bottom: 5px; }
        .main-blog .post_detail .content ul li {
          margin-left: 30px; }
  .main-blog .subsection .social {
    display: flex;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    margin-top: 1rem; }
    .main-blog .subsection .social li {
      display: flex;
      align-items: center;
      justify-content: space-between;
      -ms-flex-align: center;
      display: -ms-flexbox;
      -ms-flex-pack: space-between;
      margin-right: 2rem; }
      .main-blog .subsection .social li span {
        display: flex;
        width: 40px;
        height: 40px;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        border-radius: 50%;
        background: #3282b8;
        color: #fff;
        transition: .3s; }
      .main-blog .subsection .social li span:hover {
        transform: scale(1.1); }
      .main-blog .subsection .social li p {
        margin-left: 10px;
        position: static; }
    .main-blog .subsection .social li.like span {
      cursor: pointer; }
    .main-blog .subsection .social li.like span:hover {
      color: tomato; }
  .main-blog .share_icons {
    margin-top: 3rem; }
    .main-blog .share_icons h3 {
      text-transform: uppercase;
      font-weight: bolder;
      font-size: 1.7rem;
      font-family: 'RobotoSlab-Bold';
      color: #3282b8; }
    .main-blog .share_icons .social {
      display: flex;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      margin: 1rem 0; }
      .main-blog .share_icons .social a {
        display: flex;
        width: 60px;
        height: 60px;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        border-radius: 50%;
        background: #3282b8;
        color: #fff;
        transition: .3s;
        margin-right: 1rem;
        font-size: 1.5rem; }
      .main-blog .share_icons .social a:hover {
        background: #1b262c; }

.main-blog.detailed {
  display: block; }
  .main-blog.detailed .posts {
    margin-top: 3rem;
    max-width: 1000px; }
    .main-blog.detailed .posts h3 {
      font-family: 'RobotoSlab-Bold';
      text-transform: uppercase;
      font-size: 2rem;
      font-weight: bolder;
      color: #3282b8; }
    .main-blog.detailed .posts .contents {
      display: flex;
      flex-wrap: wrap;
      align-items: flex-start;
      -ms-flex-align: flex-start;
      display: -ms-flexbox; }
      .main-blog.detailed .posts .contents .card {
        margin: 1rem 10px; }
    .main-blog.detailed .posts a.last {
      padding: 10px 15px;
      border-radius: 4px;
      border: 2px solid #3282b8;
      color: #3282b8;
      transition: .3s;
      margin: 1rem 10px;
      display: inline-block;
      font-weight: bold; }
    .main-blog.detailed .posts a.last:hover {
      background: #3282b8;
      color: #fff; }

#comment {
  margin-top: 3rem; }
  #comment form {
    max-width: 400px;
    margin-bottom: 3rem; }
    #comment form legend {
      font-size: 1.7rem;
      font-family: 'RobotoSlab-Bold';
      color: #3282b8;
      text-transform: uppercase; }
    #comment form fieldset {
      border: none;
      margin: 1rem 0; }
      #comment form fieldset label {
        display: block;
        font-weight: bold;
        margin-bottom: 10px; }
      #comment form fieldset input, #comment form fieldset textarea {
        border: 1px solid #1b262c;
        border-radius: 5px;
        padding: 10px;
        transition: .3s;
        font-size: 1rem;
        outline: none;
        width: 100%;
        font-family: 'Monteserrat'; }
      #comment form fieldset input:active, #comment form fieldset input:focus,
      #comment form fieldset textarea:active, #comment form fieldset textarea:focus {
        border-color: #3282b8; }
      #comment form fieldset small {
        display: block;
        text-align: right;
        font-style: italic;
        color: red;
        line-height: 1rem; }
    #comment form button {
      padding: 10px 15px;
      border-radius: 25px;
      border: 2px solid #3282b8;
      font-size: 1rem;
      font-weight: bold;
      background: transparent;
      transition: .3s;
      color: #3282b8;
      display: flex;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      margin-left: auto;
      font-family: 'Monteserrat';
      cursor: pointer;
      margin-top: .5rem; }
      #comment form button span {
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        margin-right: .3rem; }
    #comment form button:hover {
      background: #3282b8;
      color: #fff; }
  #comment .comments h3 {
    text-transform: uppercase;
    font-size: 1.7rem;
    margin-bottom: 1rem;
    font-weight: bolder; }
  #comment .comments .card {
    padding: 1rem;
    max-width: 400px;
    position: relative; }
    #comment .comments .card h4 {
      font-family: 'RobotoSlab-Bold';
      font-size: 1.3rem;
      display: flex;
      align-items: center;
      -ms-flex-align: center;
      display: -ms-flexbox;
      color: #3282b8;
      text-transform: capitalize; }
      #comment .comments .card h4 span {
        display: flex;
        width: 40px;
        height: 40px;
        align-items: center;
        justify-content: center;
        -ms-flex-align: center;
        display: -ms-flexbox;
        -ms-flex-pack: center;
        border-radius: 50%;
        background: #3282b8;
        color: #fff;
        margin-right: .4rem;
        font-size: 1.1rem; }
    #comment .comments .card p {
      line-height: 1.5rem;
      font-size: 1rem;
      margin: 10px 0; }
    #comment .comments .card .date {
      display: block;
      text-align: left;
      color: #0f4c75; }
    #comment .comments .card .reply_cta {
      padding: 5px 10px;
      border-radius: 20px;
      background: grey;
      color: #fff;
      font-size: .7rem;
      position: absolute;
      right: 10px;
      bottom: 10px;
      transition: .3s; }
    #comment .comments .card .reply_cta:hover {
      transform: scale(1.1);
      background: #0f4c75;
      color: #bbe1fa; }
    #comment .comments .card .reply {
      margin-top: 1rem;
      width: 90%;
      margin-left: auto; }
      #comment .comments .card .reply h4 {
        justify-content: flex-end;
        -ms-flex-pack: flex-end;
        color: #0f4c75; }
        #comment .comments .card .reply h4 img {
          object-fit: cover;
          object-position: center;
          width: 40px;
          height: 40px;
          border-radius: 50%;
          margin-right: .4rem;
          filter: grayscale(0.4); }
      #comment .comments .card .reply p {
        text-align: right;
        color: grey; }
      #comment .comments .card .reply .date {
        text-align: right; }
  #comment .comments .card:nth-child(even) {
    border: 1px solid #0f4c75;
    border-left: none;
    border-right: none; }

.pagination .btn {
  border-color: #3282b8;
  color: #3282b8;
  margin: 3px; }
.pagination .btn.active {
  background: #3282b8;
  color: #fff; }
.pagination .btn:hover {
  background: #3282b8;
  color: #fff; }

@media (max-width: 1195px) {
  .learnmore.two .text {
    text-align: left; }
    .learnmore.two .text h2 {
      margin-left: 0; }
    .learnmore.two .text h2::after {
      margin-left: 0;
      margin-right: auto; } }
@media (max-width: 1160px) {
  #solutions {
    flex-direction: column; }
    #solutions .text {
      margin-bottom: 3rem; }
      #solutions .text h2 {
        text-align: left;
        margin-left: 0; }
      #solutions .text p {
        text-align: left;
        margin-left: 0; }
      #solutions .text .cta {
        margin-left: 0; } }
@media (max-width: 1100px) {
  #benefits .benefits:nth-child(even) .text {
    text-align: right; }
    #benefits .benefits:nth-child(even) .text p {
      margin-left: auto; }
    #benefits .benefits:nth-child(even) .text a {
      margin-right: 0;
      margin-left: auto; }

  #problems {
    flex-direction: column; }
    #problems .text {
      margin-bottom: 3rem; } }
@media (max-width: 1012px) {
  .project .imagex .con::before {
    left: 50%;
    transform: translate3d(-50%, -30%, 0); }
  .project .imagex .con::after {
    left: 50%;
    transform: translate3d(-50%, -70%, 0); }

  @keyframes animation {
    from {
      opacity: 0;
      transform: translateY(15px); }
    to {
      opacity: 1;
      transform: translateY(0px); } }
  .hamburger-menu-container {
    display: flex;
    display: -ms-flexbox; }

  #check {
    display: block; }

  .nav-btn {
    position: fixed;
    top: 4.3rem;
    height: calc(100vh - 3rem);
    width: 100%;
    left: 0;
    background-color: #69bde7;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    -ms-flex-align: center;
    -ms-flex-pack: space-between;
    overflow-y: auto;
    overflow-x: hidden;
    transform: translateX(100%);
    transition: .65s; }

  #check:checked ~ .nav-btn {
    transform: translateX(0); }

  #check:checked ~ .nav-btn .nav-link,
  #check:checked ~ .nav-btn .log-sign {
    animation: animation 0.5s ease forwards var(--i); }

  .nav-links {
    flex: initial;
    width: 100%; }

  .nav-link {
    width: 100%;
    opacity: 0;
    transform: translateY(15px); }

  .nav-link > a {
    line-height: 1;
    padding: 1.6rem 2rem; }

  .nav-link:hover > a {
    transform: scale(1);
    background: #50a9d6; }

  .log-sign {
    flex: initial;
    width: 100%; }

  .nav-links > ul {
    flex-direction: column;
    margin: 0; }

  .dropdown, .dropdown.second {
    position: initial;
    top: initial;
    left: initial;
    width: 100%;
    transform: initial;
    opacity: 1;
    pointer-events: auto;
    padding: 0;
    background: #3183ac;
    display: none; }

  .nav-link:hover > .dropdown,
  .dropdown-link:hover > .dropdown {
    display: block; }

  .nav-link:hover > a > .svg-inline--fa.fa-w-10,
  .dropdown-link:hover > a > .svg-inline--fa.fa-w-10 {
    transform: rotate(360deg); }

  .dropdown-link > a {
    background: transparent;
    color: #fff;
    padding: 1.2rem 2rem;
    line-height: 1; }

  .dropdown.second .dropdown-link > a {
    padding-left: 3rem; }

  .dropdown.second .dropdown.second .dropdown-link > a {
    padding-left: 4rem; }

  .dropdown-link:not(:nth-last-child(2)) {
    border-bottom: none; }

  .arrow {
    z-index: 1;
    background: #69bde7;
    left: 10%;
    transform: scale(1.1) rotate(45deg);
    transition: .5s; }

  .nav-link:hover .arrow {
    background: #50a9d6; }

  .dropdown .dropdown .arrow {
    display: none; }

  .dropdown-link:hover > a {
    background: #3a91bd; }

  .dropdown-link:first-child:hover ~ .arrow {
    background: #50a9d6; }

  .nav-link > a > .svg-inline--fa.fa-w-10 {
    font-size: 1.1rem;
    transform: rotate(-90deg);
    transition: .7s; }

  .dropdown .svg-inline--fa.fa-w-10 {
    font-size: 1.1rem;
    transition: .7s; }

  .log-sign {
    flex: initial;
    width: 100%;
    padding: 1.5rem 1.9rem;
    justify-content: flex-start;
    opacity: 0;
    transform: translateY(15px);
    -ms-flex-pack: flex-start; } }
@media (max-width: 978px) {
  .imagex .con::before {
    left: 50%;
    transform: translate3d(-50%, -30%, 0); }
  .imagex .con::after {
    left: 50%;
    transform: translate3d(-50%, -70%, 0); }

  .services .head, .features .head, .faqs .head {
    display: block; }
    .services .head .quote, .features .head .quote, .faqs .head .quote {
      margin-top: 3rem; }

  .features .contents .card {
    margin: 2rem 1rem; }

  .company {
    flex-direction: column;
    align-items: center;
    -ms-flex-align: center; }
    .company .details {
      margin-top: 2rem; }

  .subhero .overlay.blog_mode .one {
    bottom: 8rem; } }
@media (max-width: 842px) {
  #benefits .benefits {
    justify-content: center;
    -ms-flex-pack: center;
    flex-wrap: wrap; }

  .safety {
    background: url(../images/Metal_OES_Icon.jpg);
    background-repeat: no-repeat;
    background-size: cover; }
    .safety .design {
      display: none; }
    .safety .container .text {
      background: rgba(50, 130, 184, 0.85); }
    .safety .container .image {
      position: absolute; }
      .safety .container .image img {
        display: none; }
      .safety .container .image .social-icons {
        left: 50% !important;
        bottom: -20rem;
        transform: translateX(-50%) !important; }

  #hero .image {
    clip-path: none;
    height: 100%;
    position: absolute;
    width: 100%;
    z-index: 1; }
    #hero .image .social-icons {
      display: none; }
  #hero .text {
    position: relative;
    z-index: 2;
    background: rgba(27, 38, 44, 0.92); }
    #hero .text .social-icons {
      display: flex;
      position: relative;
      right: 0;
      bottom: 0;
      margin-top: 2rem;
      display: -ms-flexbox; } }
@media (max-width: 767px) {
  #problems .list, #solutions .list {
    width: auto;
    height: auto;
    clip-path: none;
    padding: 1rem;
    border-top: 6px solid red; }

  #solutions .list {
    border-top: 6px solid #4caf50; }

  #benefits .benefits {
    display: block; }
    #benefits .benefits .text {
      text-align: left !important;
      max-width: 450px;
      margin: 0 auto;
      margin-top: 5rem; }
      #benefits .benefits .text p {
        margin-left: 0 !important; }
      #benefits .benefits .text a {
        margin-right: 0 !important;
        margin-left: 0 !important; }

  .project {
    flex-direction: column; }
    .project .text {
      margin-bottom: 5rem; } }
@media (max-width: 580px) {
  .company .details .data .key::before {
    display: none; }

  .subhero {
    clip-path: polygon(0 0, 100% 0, 100% 95%, 60% 95%, 50% 100%, 40% 95%, 0 95%); }

  .ask .text h2 {
    font-size: 2.7rem; }

  .structure .box {
    height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    -ms-flex-align: center;
    display: -ms-flexbox;
    -ms-flex-pack: center; }
    .structure .box .circle {
      min-width: 200px;
      max-width: 200px;
      min-height: 200px;
      position: static;
      transform: none !important;
      margin: 1rem 0; } }
@media (max-width: 500px) {
  .history .side span {
    font-size: 20rem; }
  .history .side .tiny {
    width: 50px;
    height: 50px;
    transform: translate3d(-110%, -110%, 0); }
  .history .side:hover .tiny {
    transform: scale(1.7) translate3d(-65%, -65%, 0);
    filter: grayscale(0); } }
@media (max-width: 471px) {
  .gallery .contents img {
    width: 300px;
    height: 350px; } }
@media (max-width: 450px) {
  #hero .text {
    padding: 4rem 2rem; }
    #hero .text .cta {
      flex-wrap: wrap; }

  #problems, #solutions {
    padding: 4rem 1rem; }
    #problems .text .cta, #solutions .text .cta {
      flex-wrap: wrap; }
    #problems .text h2, #solutions .text h2 {
      font-size: 2.5rem; }

  #benefits, .services, .features, .faqs {
    padding: 4rem 1rem; }
    #benefits .head h2, .services .head h2, .features .head h2, .faqs .head h2 {
      font-size: 2.5rem; }

  .safety .container .text {
    padding: 4rem 1rem; }
    .safety .container .text h2 {
      font-size: 3rem; }
    .safety .container .text .cta .small {
      display: block;
      margin-top: 1rem; }

  .imagex .con:hover img {
    transform: unset; }

  .features .contents .card, .faqs .contents .card {
    border-radius: 35px; }

  .features .contents .card {
    border-radius: 35px;
    max-width: 350px;
    height: auto;
    min-height: 350px;
    transform: none !important; } }
@media (max-width: 388px) {
  .logo-container {
    margin-left: -0.9rem; }
    .logo-container .logo {
      font-size: 1.5rem; }

  #check {
    right: 1rem; }

  .container {
    padding: 0.3rem 1.1rem; }

  .company .details .data {
    display: block;
    margin: 2rem 0; }
    .company .details .data .key {
      margin: .5rem 0; }

  #hero .text {
    padding: 4rem 1rem; }
    #hero .text h1 {
      font-size: 3rem; }
    #hero .text .cta {
      flex-wrap: wrap; }

  #problems .text .cta .small, #solutions .text .cta .small {
    margin-left: 0;
    margin-top: 1rem; }
  #problems .text h2, #solutions .text h2 {
    font-size: 2rem; }

  #newsletter .letter {
    padding: 6rem 1rem; }
    #newsletter .letter h2 {
      font-size: 3rem; }

  .allservices .head h2 {
    font-size: 2.5rem; } }
@media (max-width: 338px) {
  .company .image img {
    width: 250px;
    height: 250px; }

  .gallery .contents img {
    width: 200px;
    height: 250px; }

  .features .contents .card h3 {
    font-size: 1.2rem; }

  .history .side span {
    font-size: 14rem; }
  .history .side .tiny {
    width: 35px;
    height: 35px; } }
@media (max-width: 320px) {
  .subhero .overlay h1 {
    font-size: 3.5rem; }

  .project .text h2 {
    font-size: 2.5rem; }

  #hero .text {
    padding: 4rem 1rem; }
    #hero .text h1 {
      font-size: 3rem; }
    #hero .text .cta {
      flex-wrap: wrap; }
      #hero .text .cta .small {
        margin-left: 0;
        margin-top: 1rem; }

  .features .contents .card {
    padding: 2rem 1rem; }

  .faqs .head h2 {
    font-size: 2rem; }

  .safety .container .text h2 {
    font-size: 2.5rem; }

  .structure h2, .ethos h2 {
    font-size: 2.2rem; }

  #problems .list ul li .icon, #solutions .list ul li .icon {
    font-size: 1.5rem;
    min-width: 30px; } }
#ftco-loader {
  display: none;
  position: fixed;
  width: 96px;
  height: 96px;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  background-color: rgba(255, 255, 255, 0.9);
  -webkit-box-shadow: 0px 24px 64px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 24px 64px rgba(0, 0, 0, 0.24);
  border-radius: 16px;
  opacity: 0;
  visibility: hidden;
  -webkit-transition: opacity .2s ease-out, visibility 0s linear .2s;
  -o-transition: opacity .2s ease-out, visibility 0s linear .2s;
  transition: opacity .2s ease-out, visibility 0s linear .2s;
  z-index: 100000; }

#ftco-loader.fullscreen {
  padding: 0;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  -webkit-transform: none;
  -ms-transform: none;
  transform: none;
  background-color: #fff;
  border-radius: 0;
  -webkit-box-shadow: none;
  box-shadow: none; }

#ftco-loader.show {
  -webkit-transition: opacity .4s ease-out, visibility 0s linear 0s;
  -o-transition: opacity .4s ease-out, visibility 0s linear 0s;
  transition: opacity .4s ease-out, visibility 0s linear 0s;
  visibility: visible;
  opacity: 1; }

#ftco-loader .circular {
  -webkit-animation: loader-rotate 2s linear infinite;
  animation: loader-rotate 2s linear infinite;
  position: absolute;
  left: calc(50% - 24px);
  top: calc(50% - 24px);
  display: block;
  -webkit-transform: rotate(0deg);
  -ms-transform: rotate(0deg);
  transform: rotate(0deg); }

#ftco-loader .path {
  stroke-dasharray: 1, 200;
  stroke-dashoffset: 0;
  -webkit-animation: loader-dash 1.5s ease-in-out infinite;
  animation: loader-dash 1.5s ease-in-out infinite;
  stroke-linecap: round; }

@-webkit-keyframes loader-rotate {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg); } }
@keyframes loader-rotate {
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg); } }
@-webkit-keyframes loader-dash {
  0% {
    stroke-dasharray: 1, 200;
    stroke-dashoffset: 0; }
  50% {
    stroke-dasharray: 89, 200;
    stroke-dashoffset: -35px; }
  100% {
    stroke-dasharray: 89, 200;
    stroke-dashoffset: -136px; } }
@keyframes loader-dash {
  0% {
    stroke-dasharray: 1, 200;
    stroke-dashoffset: 0; }
  50% {
    stroke-dasharray: 89, 200;
    stroke-dashoffset: -35px; }
  100% {
    stroke-dasharray: 89, 200;
    stroke-dashoffset: -136px; } }

/*# sourceMappingURL=style.css.map */

'''
h = '''-ms-transform: translateY(-50%);
  -webkit-transform: translateY(-50%);'''
import re

pattern = 'transform'

# x = re.finditer(pattern, s)
# for i in x:
# 	print(i)

# print(s[1])
# print(dir(re))
# print(dir(''))
li=s.split('\n')
newl=[]
for i in li:
	i=i.strip(';')
	if re.search(pattern, i):
		print(23,i.split(':'))
		x=i.split(':')[-1]
		newl.append(i+';\n')
		newl.append("-ms-transform: "+x+';\n')
		newl.append("-webkit-transform: "+x+';\n')
	else:
		newl.append(i+';\n')
text = ''
for i in newl:
	text+=i

with open('cssas.css','w') as f:
	f.write(text)
