def get_style():
    return """
    <style>
            body {
                margin: 0;
                padding: 0;
                line-height: 1.6;
                color: #000;
                font-family: Roboto,sans-serif;
                font-weight: 400;
                font-size: 15px;
                font-smoothing: antialiased;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
                text-rendering: optimizeLegibility;
                overflow-anchor: none
            }

            a {
                color: #0029ad;
                text-decoration: none
            }

            img {
                border: none;
                max-width: 100%
            }

            li,ul {
                margin: 0;
                padding: 0;
                list-style: none
            }

            h1,h2,h3,h4,h5,h6 {
                font-family: sans-serif;
                margin: 0;
                padding: 0;
                line-height: 1.4;
                font-weight: bold
            }

            applet,blockquote,canvas,caption,dd,dl,dt,embed,fieldset,figcaption,figure,hgroup,iframe,object,ol,output,p,pre,strike,sub,summary,sup,table,tbody,td,tfoot,th,thead,time,tr,video {
                border: 0;
                margin: 0;
                padding: 0
            }

            * {
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box
            }

            ::after,::before {
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box
            }

            button,input,select,textarea {
                font-family: Roboto,sans-serif;
                font-size: 14px;
                font-weight: 400;
                line-height: inherit;
                outline: 0
            }

            input,select {
                height: 40px;
                padding: 0 10px
            }

            input,select,textarea {
                float: left;
                width: 100%;
                border: solid .5px #eaeaea;
                margin: 0;
                box-shadow: none;
                -webkit-appearance: none;
                -moz-appearance: none;
                -o-appearance: none;
                text-overflow: "";
                appearance: none;
                border-radius: 2px;
                webkit-border-radius: 2px;
                -moz-border-radius: 2px
            }

            select {
                background: url(../images/arow.svg) no-repeat;
                background-position: right 8px top 50%;
                padding-right: 24px
            }

            .form-group {
                float: left;
                width: 100%;
                position: relative;
                margin-bottom: 15px;
                display: table
            }

            .form-group:last-child {
                margin-bottom: 0
            }

            .btn {
                display: inline-block;
                padding: 0 16px;
                height: 40px;
                line-height: 40px;
                background-color: #dddfe2;
                cursor: pointer;
                text-align: center;
                border-radius: 2px;
                -webkit-border-radius: 2px;
                -moz-border-radius: 2px
            }

            button {
                background: 0 0;
                cursor: pointer;
                border: 0;
                padding: 0;
                margin: 0
            }

            table {
                border-collapse: collapse;
                border-spacing: 0;
                width: 100%
            }

            table td,table th {
                padding: 3px;
                border: solid 1px #dddfe2
            }

            table thead th {
                background: #f0f8ff;
                font-size: 14px;
                font-weight: 500
            }

            .text-danger {
                width: 100%;
                float: left;
                font-size: 12px;
                text-align: right;
                color: #ed1c25;
                padding-top: 5px;
                font-style: italic
            }

            .btn-right {
                float: right
            }

            .main {
                float: left;
                width: 100%;
                position: relative;
                margin-bottom: 20px
            }

            .main-content {
                margin: auto;
                width: 100%;
                max-width: 1140px;
                min-width: 240px
            }

            .content-left {
                float: left;
                width: 53.5%;
                position: relative;
                padding-right: 16px
            }

            @media only screen and (max-width: 1024px) {
                .main-content {
                    max-width:1000px
                }

                .content-left {
                    width: 52.5%
                }
            }

            .header {
                float: left;
                width: 100%;
                position: relative;
                margin-bottom: 16px
            }

            .header-pc {
                float: left;
                width: 100%
            }

            .header-content {
                float: left;
                width: 100%;
                padding: 5px 0;
                background: #fff
            }

            .header-logo {
                float: left
            }

            .header-logo-img {
                float: left
            }

            .header-right {
                float: left;
                margin-left: 20px;
                border-left: solid 1px #e0e0e0;
                padding-left: 21px;
                margin-top: 14px
            }

            .icon-menu {
                top: 2px;
                position: relative
            }

            .header-time {
                font-family: sans-serif;
                float: right;
                color: #666;
                font-size: 14px
            }

            .btn-calendar {
                display: none;
                position: absolute;
                right: 16px;
                top: 10px;
                width: 36px;
                height: 36px;
                text-align: center
            }

            .icon-calendar {
                position: relative;
                top: 8px
            }

            @media only screen and (max-width: 960px) {
                .widget {
                    margin-bottom:12px
                }

                .aside-300 {
                    float: left;
                    width: 100%;
                    display: none
                }

                .aside-160 {
                    width: 100%;
                    display: none
                }

                .header {
                    margin-bottom: 12px
                }

                .header-content {
                    background: #fff;
                    position: relative;
                    z-index: 9
                }

                .content-left {
                    width: 100%;
                    padding: 0
                }

                .headermobi {
                    padding: 0;
                    height: 56px
                }

                .header-logo-img {
                    float: none;
                    height: 36px;
                    top: 12px;
                    position: relative
                }

                .header-logo {
                    float: left;
                    width: 100%;
                    text-align: center
                }

                .btn-calendar {
                    display: block
                }

                .header-time {
                    display: none
                }
            }

            .aside-300 {
                float: right;
                width: 27%;
                position: relative;
                overflow: hidden
            }

            .aside-160 {
                float: left;
                width: 18%;
                position: relative
            }

            .widget {
                float: left;
                width: 100%;
                margin-bottom: 16px;
                box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -webkit-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -moz-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12)
            }

            .widget-title {
                float: left;
                width: 100%;
                position: relative;
                padding: 10px 12px;
                background: #f0f8ff;
                text-transform: uppercase;
                border-bottom: solid .5px #eaeaea
            }

            .widget-title a {
                color: #000
            }

            .widget-container {
                float: left;
                width: 100%;
                position: relative
            }

            .widget-title h3 {
                font-size: 13px
            }

            .link-item a {
                font-family: sans-serif;
                float: left;
                width: 100%;
                padding: 6px 12px 6px 24px;
                position: relative
            }

            .link-item a::before {
                border-top: 4px dashed;
                border-right: 4px solid transparent;
                border-left: 4px solid transparent;
                content: "";
                position: absolute;
                left: 10px;
                top: 17px;
                color: #444;
                -webkit-transform: rotate(-90deg);
                -moz-transform: rotate(-90deg);
                -ms-transform: rotate(-90deg);
                -o-transform: rotate(-90deg);
                transform: rotate(-90deg)
            }

            .link-item2 {
                font-family: sans-serif;
                float: left;
                width: 100%;
                padding: 6px 12px 6px 24px;
                position: relative;
                font-weight: 500
            }

            .link-item2::before {
                border-top: 4px dashed;
                border-right: 4px solid transparent;
                border-left: 4px solid transparent;
                content: "";
                position: absolute;
                left: 10px;
                top: 17px;
                color: #444;
                -webkit-transform: rotate(-90deg);
                -moz-transform: rotate(-90deg);
                -ms-transform: rotate(-90deg);
                -o-transform: rotate(-90deg);
                transform: rotate(-90deg)
            }

            .link-item2-sub a {
                font-family: sans-serif;
                float: left;
                width: 100%;
                padding: 5px 5px 5px 24px
            }

            .widget_bg {
                background: #c80505;
                color: #fff
            }

            .form-wg {
                width: 100%;
                float: left;
                padding: 16px
            }

            .label_gril {
                float: left;
                line-height: 40px;
                width: 70px
            }

            .input_gril {
                display: grid
            }

            .tutorial-loto {
                color: #555;
                font-size: 13px;
                line-height: 22px;
                font-style: italic
            }

            .user-sidebar {
                background: #f0f8ff;
                position: relative;
                padding: 0 16px 10px 16px;
                float: left;
                width: 100%
            }

            .logosidebar {
                height: 48px
            }

            .pushbar_locked {
                overflow: hidden;
                height: 100vh;
                position: fixed;
                width: 100%
            }

            .pushbar {
                background: #fff;
                z-index: 99999;
                position: fixed;
                will-change: transform;
                overflow-y: auto;
                transition: transform .5s ease;
                will-change: transform
            }

            .pushbar_overlay {
                z-index: -999;
                position: fixed;
                width: 100%;
                max-width: 100%;
                height: 100%;
                min-height: 100vh;
                top: 0;
                left: 0;
                will-change: opacity;
                opacity: 0;
                will-change: opacity;
                background: #3c3442
            }

            .pushbar_locked .pushbar_overlay {
                opacity: .8;
                z-index: 999;
                transition: opacity .5s ease
            }

            .pushbar.from_left {
                top: 0;
                left: 0;
                width: 300px;
                max-width: 100%;
                height: 100%;
                overflow-x: hidden;
                transform: translateZ(0) translateX(-100%)
            }

            .pushbar.opened {
                transform: translateX(0) translateY(0)
            }

            .btn-pushbar-close {
                height: 48px;
                position: relative;
                z-index: 99;
                font-size: 30px;
                cursor: pointer;
                background: #f0f8ff;
                width: 100%;
                float: left
            }

            .btn-pushbar-3 {
                cursor: pointer;
                position: absolute;
                left: 8px;
                top: 10px;
                width: 36px;
                height: 36px;
                line-height: 36px;
                text-align: center;
                border-radius: 100%;
                display: none
            }

            .pushbar-hide {
                display: none
            }

            .icon-back {
                height: 16px;
                width: 16px;
                position: relative;
                left: 16px;
                top: -2px
            }

            @media only screen and (max-width: 960px) {
                .pushbar-hide {
                    display:block
                }

                .btn-pushbar-3 {
                    display: block
                }
            }

            .ac-menu {
                width: 100%;
                float: left
            }

            .ac_item {
                position: relative;
                width: 100%;
                float: left
            }

            .ac_item:last-child {
                border-bottom: 0
            }

            .ac_content {
                display: none;
                width: 100%;
                float: left
            }

            .ac_icon {
                cursor: pointer;
                display: block;
                position: absolute;
                right: 10px;
                background-size: 12px;
                width: 36px;
                height: 36px;
                z-index: 2;
                top: 6px
            }

            .ac_icon::before {
                border-top: 4px dashed;
                border-right: 4px solid transparent;
                border-left: 4px solid transparent;
                content: "";
                left: 40%;
                top: 50%;
                position: absolute;
                color: #666;
                transition: all .4s ease-out;
                -webkit-transition: all .4s ease-out
            }

            .ac_open .ac_icon::before {
                -webkit-transform: rotate(180deg);
                -moz-transform: rotate(180deg);
                -ms-transform: rotate(180deg);
                -o-transform: rotate(180deg);
                transform: rotate(180deg);
                transition: all .4s ease-out;
                -webkit-transition: all .4s ease-out
            }

            .ac_title_2 {
                font-size: 16px;
                float: left;
                padding: 12px 36px 12px 56px;
                width: 100%;
                font-weight: 500;
                color: #222
            }

            .ac_ul2 {
                padding-bottom: 10px;
                float: left;
                width: 100%
            }

            .ac_ul2 a {
                padding: 10px 36px 10px 56px;
                float: left;
                width: 100%;
                color: #222
            }

            .ic-m {
                width: 24px;
                float: left;
                position: absolute;
                left: 16px
            }

            .ac_item.boder_top {
                border-top: solid .5px #eaeaea
            }

            .ac_item.ac_open .ac_title_2 {
                color: #ed1c25
            }

            .menu_ul {
                width: 100%;
                margin: auto;
                max-width: 1140px
            }

            .menu_li {
                float: left;
                position: relative
            }

            .menu_a {
                font-family: sans-serif;
                padding: 0 14px;
                float: left;
                width: 100%;
                height: 48px;
                line-height: 48px;
                font-size: 14px;
                text-transform: uppercase;
                color: #fff;
                font-weight: bold
            }

            .menu_a:hover {
                background: #ed1c25;
                color: #fff
            }

            .menu_down li {
                width: 100%
            }

            .menu_down {
                width: 180px;
                background: #fff;
                position: absolute;
                opacity: 0;
                visibility: hidden;
                z-index: 99999;
                box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -webkit-transition: opacity .2s linear,visibility .2s linear;
                -moz-transition: opacity .2s linear,visibility .2s linear;
                -o-transition: opacity .2s linear,visibility .2s linear;
                transition: opacity .2s linear,visibility .2s linear;
                top: 48px;
                left: 0
            }

            .menu_down a {
                padding: 8px 15px;
                float: left;
                width: 100%;
                position: relative;
                color: #222
            }

            .menu_down a:hover {
                background: #f0f8ff
            }

            .icon-home {
                width: 17px;
                height: 16px;
                max-width: 17px;
                position: relative;
                top: 2px
            }

            @media only screen and (max-width: 1140px) {
                .menu_ul {
                    overflow-y:hidden;
                    -webkit-overflow-scrolling: touch;
                    overflow-x: scroll;
                    overflow-x: auto;
                    white-space: nowrap;
                    display: flex
                }

                .menu_li {
                    display: table-cell;
                    text-align: center;
                    position: inherit
                }
            }

            .nav_header {
                background: #c80505;
                float: left;
                width: 100%;
                position: relative
            }

            .nav-scrol-link-ic {
                position: absolute;
                cursor: pointer;
                left: 0;
                width: 40px;
                text-align: center;
                background: #c80505;
                z-index: 99;
                line-height: 48px;
                height: 48px;
                color: #fff;
                display: none
            }

            @media only screen and (max-width: 960px) {
                .nav_header {
                    background:#c80505
                }

                .hide {
                    display: none
                }
            }

            .footer {
                float: left;
                width: 100%;
                position: relative;
                background: #f0f8ff;
                border-top: solid .5px #dddfe2
            }

            .footer-content {
                padding: 15px 0;
                float: left;
                width: 100%
            }

            .copyright {
                float: left;
                font-size: 13px;
                line-height: 24px;
                width: 70%
            }

            .share-socal {
                float: right;
                position: relative;
                width: 30%;
                text-align: center
            }

            .rows-add {
                position: relative;
                padding-top: 16px;
                width: 100%;
                float: left
            }

            .textic24 {
                font-weight: 700
            }

            .ic24 {
                position: relative;
                top: 5px;
                margin-right: 5px
            }

            .dmca_protected {
                margin-left: 10px;
                float: left;
                margin-top: 5px
            }

            .mxh-like-item {
                float: left;
                margin-left: 10px
            }

            .link-web {
                color: #999;
                float: left;
                font-size: 13px;
                width: 100%
            }

            .link-web > a {
                color: #555;
                font-size: 13px
            }

            .icon-face {
                border-radius: 100%;
                float: left;
                color: #fff;
                height: 30px;
                line-height: 30px;
                text-align: center;
                width: 30px
            }

            .icon-face.cl1 {
                background: #134a8d;
                color: #fff
            }

            .icon-face.cl2 {
                background: #ed3b3b;
                color: #fff
            }

            .icon-face.cl3 {
                background: #10afe3;
                color: #fff
            }

            .nav-bottom a {
                margin-right: 16px;
                color: #000
            }

            .nav-bottom {
                padding-top: 16px;
                font-size: 14px;
                font-weight: 500
            }

            .nav_hidden {
                transform: translateY(-100%);
                -webkit-transform: translateY(-100%);
                -moz-transform: translateY(-100%);
                -o-transform: translateY(-100%);
                transition: transform .3s ease;
                -webkit-transition: transform .3s ease;
                -moz-transition: transform .3s ease;
                -o-transition: transform .3s ease
            }

            .nav_show {
                z-index: 99;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                transform: translateY(0);
                -webkit-transform: translateY(0);
                -moz-transform: translateY(0);
                -o-transform: translateY(0);
                transition: transform .3s ease;
                -webkit-transition: transform .3s ease;
                -moz-transition: transform .3s ease;
                -o-transition: transform .3s ease
            }

            .backtotop {
                background-color: #ed1c25;
                position: fixed;
                bottom: 10px;
                right: 10px;
                z-index: 999;
                border-radius: 100%;
                height: 48px;
                width: 48px;
                line-height: 48px;
                text-align: center;
                box-shadow: 0 1px 6px 0 rgba(32,33,36,.28);
                display: none;
                animation: animatezoom .6s
            }

            @keyframes animatezoom {
                from {
                    transform: scale(0)
                }

                to {
                    transform: scale(1)
                }
            }

            .show_backtotop {
                display: block
            }

            @media only screen and (max-width: 960px) {
                .footer {
                    padding:0 12px
                }

                .nav-bottom {
                    padding-top: 8px
                }

                .nav-bottom a {
                    padding-top: 10px;
                    display: inline-block
                }

                .copyright {
                    width: 100%
                }

                .share-socal {
                    float: left;
                    width: 100%
                }

                .backtotop {
                    bottom: 110px
                }
            }

            .section {
                float: left;
                width: 100%;
                margin-bottom: 16px;
                position: relative;
                box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -webkit-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -moz-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12)
            }

            .section:last-child {
                margin-bottom: 0
            }

            .section-header {
                float: left;
                width: 100%;
                position: relative;
                background: #ffeca0;
                border: solid .5px #dddfe2;
                border-bottom: 0;
                padding: 8px 0;
                text-align: center
            }

            .section-header h1 {
                font-family: sans-serif;
                font-size: 18px;
                text-align: center;
                font-weight: bold
            }

            .section-header h2 {
                font-size: 18px;
                text-align: center;
                font-weight: 700
            }

            .section-header h3 {
                font-size: 18px;
                text-align: center;
                font-weight: 700
            }

            .section-header h2>a,.section-header h3>a {
                color: #ed1c25
            }

            .section-header2 {
                float: left;
                width: 100%;
                position: relative;
                background: #f0f8ff;
                border: solid .5px #dddfe2;
                padding: 8px 10px
            }

            .section-header2 h2 {
                font-size: 16px;
                font-weight: 700
            }

            .section-header2 h2>a {
                color: #ed1c25
            }

            .section-header2 h2>a:hover {
                color: #0029ad
            }

            .section-content {
                float: left;
                width: 100%;
                position: relative
            }

            .color_red {
                color: #ed1c25
            }

            header div:last-child {
                margin-bottom: 0
            }

            .image {
                width: 100%;
                float: left;
                object-fit: cover
            }

            .description {
                display: grid
            }

            .post-news li {
                float: left;
                width: 100%;
                padding: 10px;
                border-bottom: solid .5px #dddfe2;
                position: relative
            }

            .post-title2 {
                font-size: 16px;
                font-weight: 400;
                padding-left: 16px
            }

            .post-news a {
                color: #000
            }

            .post-news a:hover {
                color: #ed1c25
            }

            .section {
                float: left;
                width: 100%;
                margin-bottom: 16px;
                position: relative;
                box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -webkit-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
                -moz-box-shadow: 0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12)
            }

            .section-header h1 {
                font-family: sans-serif;
                font-size: 22px;
                text-align: center;
                font-weight: bold
            }

            .section-header h2 {
                font-size: 22px;
                text-align: center;
                font-weight: 700
            }

            .section-header h3 {
                font-size: 22px;
                text-align: center;
                font-weight: 700
            }

            .section-header h2 > a {
                font-family: sans-serif;
                color: #ed1c25
            }

            .section-header2 {
                float: left;
                width: 100%;
                position: relative;
                background: #f0f8ff;
                border: solid .5px #dddfe2;
                padding: 8px 10px
            }

            .section-header2 h2 {
                font-size: 16px;
                font-weight: 700
            }

            .section-header2 h2 > a {
                color: #ed1c25
            }

            .section-content {
                float: left;
                width: 100%;
                position: relative
            }

            header div:last-child {
                margin-bottom: 0
            }

            .image {
                width: 100%;
                float: left;
                object-fit: cover
            }

            .description {
                display: grid
            }

            .post-news li {
                float: left;
                width: 100%;
                padding: 10px 16px;
                border-bottom: solid .5px #dddfe2;
                position: relative
            }

            .post-title2 {
                font-size: 16px;
                font-weight: 400
            }

            .ads {
                float: left;
                width: 100%;
                text-align: center;
                position: relative;
                margin-bottom: 16px
            }

            .google-ads {
                width: 100%;
                float: left;
                text-align: center;
                margin: 12px 0
            }

            .text-center {
                text-align: center
            }

            .see-more {
                float: left;
                width: 100%;
                text-align: center;
                padding: 12px 16px
            }

            .see-more a {
                border: solid .5px #e0e0e0;
                padding: 4px 16px;
                display: inline-block;
                border-radius: 25px;
                color: #666
            }

            .see-more a:hover {
                color: #ed1c25
            }

            .post-thumbnail {
                float: left;
                margin-right: 12px;
                position: relative;
                overflow: hidden
            }

            .thumb120 {
                width: 120px;
                float: left;
                margin-right: 12px;
                position: relative;
                overflow: hidden
            }

            .thumb120 img {
                width: 100%;
                float: left;
                object-fit: cover
            }

            .paddingtop0 {
                padding-top: 0
            }

            @media only screen and (max-width: 960px) {
                .section {
                    margin-bottom:12px;
                    background: #fff
                }

                .ads {
                    margin-bottom: 12px
                }
            }

            .table-result {
                text-align: center;
                font-family: arial
            }

            .table-lottery th,.table-result td {
                padding: 0
            }

            .table-result tr:nth-of-type(2n) {
                background-color: #f0f8ff
            }

            .table-result thead th {
                background-color: #f0f8ff;
                font-weight: 500
            }

            .table-result th {
                font-weight: 400;
                font-size: 16px
            }

            .name-prize {
                width: 10%
            }

            .number-prize {
                width: 90%
            }

            .code-DB1,.code-DB10,.code-DB11,.code-DB12,.code-DB13,.code-DB14,.code-DB15,.code-DB2,.code-DB3,.code-DB4,.code-DB5,.code-DB6,.code-DB7,.code-DB8,.code-DB9 {
                float: left;
                height: 40px;
                line-height: 40px;
                color: #ed1c25;
                font-weight: 700
            }

            .code-DB10,.code-DB11,.code-DB12,.code-DB13,.code-DB14,.code-DB15,.code-DB16,.code-DB17,.code-DB18,.code-DB19,.code-DB20 {
                float: left;
                margin: 0 6px;
                color: #ed1c25;
                font-weight: 700
            }

            .code-DB1 {
                width: 100%;
                font-size: 22px
            }

            .code-DB2 {
                width: 50%;
                font-size: 22px
            }

            .code-DB3 {
                width: 33.3%;
                font-size: 22px
            }

            .code-DB4 {
                width: 25%;
                font-size: 22px
            }

            .code-DB5 {
                width: 20%;
                font-size: 22px
            }

            .code-DB6 {
                width: 16.5%;
                font-size: 20px
            }

            .code-DB7 {
                width: 14%;
                font-size: 20px
            }

            .code-DB8 {
                width: 12.5%;
                font-size: 20px
            }

            .code-DB9 {
                width: 11%;
                font-size: 20px
            }

            .code-DB10 {
                width: 20%;
                font-size: 20px
            }

            .special-prize {
                float: left;
                width: 100%;
                height: 40px;
                line-height: 40px;
                font-size: 34px;
                font-weight: 700;
                color: #ed1c25
            }

            .prize1 {
                float: left;
                width: 100%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize2 {
                float: left;
                width: 50%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize3 {
                float: left;
                width: 33.3%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize4 {
                float: left;
                width: 25%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize5 {
                float: left;
                width: 33.3%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize6 {
                float: left;
                width: 33.3%;
                height: 40px;
                line-height: 40px;
                font-size: 28px;
                font-weight: 700
            }

            .prize7 {
                float: left;
                width: 25%;
                height: 40px;
                line-height: 40px;
                font-weight: 700;
                font-size: 34px;
                color: #ed1c25
            }

            .prize-col2 {
                width: 40%
            }

            .prize-col3 {
                width: 30%
            }

            .prize-col4 {
                width: 22.5%
            }

            .xs_prize1 {
                float: left;
                width: 100%;
                height: 40px;
                line-height: 40px;
                font-size: 26px;
                font-weight: 700
            }

            .xs_prize2 {
                float: left;
                width: 50%;
                height: 40px;
                line-height: 40px;
                font-size: 26px;
                font-weight: 700
            }

            .xs_prize3 {
                float: left;
                width: 33.3%;
                height: 40px;
                line-height: 40px;
                font-size: 26px;
                font-weight: 700
            }

            .xs_prize4 {
                float: left;
                width: 25%;
                height: 40px;
                line-height: 40px;
                font-size: 26px;
                font-weight: 700
            }

            .prize_db {
                color: #ed1c25
            }

            .table-loto tr:nth-of-type(2n) {
                background-color: #f0f8ff
            }

            .table-loto td {
                font-size: 16px;
                font-weight: 700
            }

            .table-loto th {
                color: #ed1c25;
                font-weight: 400
            }

            .table-loto thead th {
                background-color: #f0f8ff;
                font-size: 14px;
                color: #000
            }

            .loto-name {
                width: 10%;
                text-align: center;
                color: #ed1c25
            }

            .loto-col2 {
                width: 40%;
                font-size: 16px;
                font-weight: 700
            }

            .loto-col3 {
                width: 30%;
                font-size: 16px;
                font-weight: 700
            }

            .loto-col4 {
                width: 22.5%;
                font-size: 16px;
                font-weight: 700
            }

            @media (max-width: 960px) {
                .prize1,.prize2,.prize3,.prize4,.prize5,.prize6 {
                    font-size:24px
                }

                .prize7 {
                    font-size: 30px
                }

                .xs_prize1,.xs_prize2,.xs_prize3,.xs_prize4 {
                    font-size: 24px
                }

                .font4tinh {
                    font-size: 22px
                }
            }

            .config-item {
                background: #f2f2f2;
                width: 48px;
                cursor: pointer
            }

            .config-item:hover {
                background: #c80505;
                color: #fff
            }

            .config-item.active {
                background: #c80505;
                color: #fff
            }

            .number-config {
                background: #f2f2f2;
                cursor: pointer
            }

            .number-config:hover {
                background: #F88825;
                color: #fff
            }

            .xs-bong {
                font-weight: 700;
                background: #F88825;
                color: #fff;
                border-radius: 4px;
                padding: 0 2px
            }

            .div-table {
                display: table;
                text-align: center;
                font-size: 13px;
                width: 100%;
                border-bottom: solid 1px #e0e0e0;
                display: none
            }

            .div-table > div {
                display: table-cell;
                border-right: solid 1px #e0e0e0
            }

            .div-table > div:last-child {
                display: table-cell;
                border-right: 0;
                padding: 4px 0
            }

            .table-tkxs {
                margin-bottom: 16px
            }

            .table-tkxs td {
                padding: 8px
            }

            .title-tkxs {
                font-size: 16px
            }

            .bg-ligh {
                background: #f9f9f9
            }

            .bg-db {
                background: #ed1c25 !important;
                color: #fff
            }

            .site-link {
                font-family: sans-serif;
                width: 100%;
                float: left;
                font-size: 14px;
                font-weight: 400;
                margin-top: 5px
            }

            .site-link a {
                font-family: sans-serif;
                display: initial;
                text-decoration: underline
            }

            .site-link a+a:before {
                font-family: sans-serif;
                padding: 0 3px;
                color: #555;
                content: "/\00a0";
                display: inline-block
            }

            h3.site-link {
                font-family: sans-serif;
                width: 100%;
                float: left;
                font-size: 14px;
                font-weight: 400;
                margin-top: 5px
            }

            h3.site-link a {
                font-family: sans-serif;
                display: initial;
                text-decoration: underline;
                color: #0029ad
            }

            h3.site-link a+a:before {
                padding: 0 3px;
                color: #555;
                content: "/\00a0";
                display: inline-block
            }

            .site-link2 {
                padding: 6px 16px;
                width: 100%;
                float: left;
                font-weight: 500
            }

            .site-link2 a {
                display: initial;
                text-decoration: underline
            }

            .site-link2 a+a:before,.site-link2 a+span:before {
                padding: 0 3px;
                color: #555;
                content: "/\00a0";
                display: inline-block
            }

            .table-result th a {
                text-decoration: underline
            }

            .table-loto th a {
                text-decoration: underline
            }

            .link-statistic {
                padding: 12px 16px;
                width: 100%;
                float: left
            }

            .link-statistic li {
                float: left;
                width: 100%;
                padding: 5px 0 5px 16px;
                position: relative
            }

            .link-statistic li::before {
                border-top: 4px dashed;
                border-right: 4px solid transparent;
                border-left: 4px solid transparent;
                content: "";
                position: absolute;
                left: 0;
                top: 15px;
                color: #444;
                -webkit-transform: rotate(-90deg);
                -moz-transform: rotate(-90deg);
                -ms-transform: rotate(-90deg);
                -o-transform: rotate(-90deg);
                transform: rotate(-90deg)
            }

            .sms-loto {
                float: left;
                width: 100%;
                border-top: dashed .5px #dddfe2;
                color: #555;
                font-size: 14px;
                padding: 12px 16px
            }

            .sms-loto p {
                color: #555
            }

            .mega-results {
                text-align: center;
                width: 100%;
                float: left
            }

            .jackpot-item {
                margin-top: 16px;
                width: 100%;
                float: left
            }

            .jackpot-bonus-vnd {
                background: #ed3b3b;
                border-radius: 25px;
                color: #fff;
                font-size: 24px;
                padding: 3px 15px;
                display: inline-block;
                font-weight: 700
            }

            .font-Jackpot {
                font-size: 18px;
                font-weight: 500
            }

            .btn-results {
                font-size: 24px;
                font-weight: 700;
                color: #ed3b3b;
                border-radius: 100%;
                border: solid 2px #dddfe2;
                display: inline-block;
                height: 44px;
                width: 44px;
                text-align: center;
                line-height: 40px
            }

            .bg_jackpot {
                background: #ffd200
            }

            .span-text {
                font-size: 14px;
                color: #222;
                font-weight: 300
            }

            .table-xsdt th {
                font-weight: 400;
                font-size: 14px;
                text-align: left;
                background: #f0f8ff;
                padding: 8px
            }

            .table-xsdt td {
                font-size: 22px;
                text-align: center;
                font-weight: 700;
                padding: 3px
            }

            .notification {
                width: 100%;
                float: left;
                background: #ffeca0;
                text-align: center;
                color: #ed1c25;
                font-weight: 500;
                font-size: 20px
            }

            .notificationnote {
                width: 100%;
                float: left;
                background: #ffeca0;
                text-align: center;
                color: #ed1c25;
                font-weight: 500;
                margin-bottom: 10px
            }

            .evenloto2 {
                animation: wg100-item .7s infinite
            }

            .wg100-item {
                background: #f44336;
                border-radius: 3px;
                color: #fff;
                padding: 5px 0;
                font-size: 14px;
                -webkit-animation: wg100-item .7s infinite;
                -moz-animation: wg100-item .7s infinite;
                -o-animation: wg100-item .7s infinite;
                animation: wg100-item .7s infinite
            }

            @-webkit-keyframes wg100-item {
                50% {
                    background: #4caf50;
                    color: #fff
                }
            }

            @-moz-keyframes wg100-item {
                50% {
                    background: #4caf50;
                    color: #fff
                }
            }

            @-o-keyframes wg100-item {
                50% {
                    background: #4caf50;
                    color: #fff
                }
            }

            @keyframes wg100-item {
                50% {
                    background: #4caf50;
                    color: #fff
                }
            }

            @-webkit-keyframes notification {
                50% {
                    background: #f2f2f2
                }
            }

            .bltt {
                text-transform: uppercase;
                padding-bottom: 6px;
                color: #ed1c25;
                position: relative;
                padding-left: 28px
            }

            .ic-live {
                position: absolute;
                left: 16px;
                top: 5px
            }

            .ic-live::before {
                border-radius: 100%;
                -webkit-border-radius: 100%;
                display: block;
                width: 12px;
                height: 12px;
                background: #ed1c25;
                position: absolute;
                right: 0;
                content: '';
                box-shadow: 0 0 0 rgba(23,143,214,.4);
                -webkit-animation: live-pulse 1s infinite;
                -moz-animation: live-pulse 1s infinite;
                -o-animation: live-pulse 1s infinite;
                animation: live-pulse 1s infinite
            }

            @-webkit-keyframes live-pulse {
                0% {
                    -webkit-box-shadow: 0 0 0 0 rgba(225,6,0,0.5)
                }

                70% {
                    -webkit-box-shadow: 0 0 0 10px rgba(225,6,0,0)
                }

                100% {
                    -webkit-box-shadow: 0 0 0 0 rgba(225,6,0,0)
                }
            }

            @keyframes live-pulse {
                0% {
                    -moz-box-shadow: 0 0 0 0 rgba(225,6,0,0.5);
                    box-shadow: 0 0 0 0 rgba(225,6,0,0.5)
                }

                70% {
                    -moz-box-shadow: 0 0 0 10px rgba(225,6,0,0);
                    box-shadow: 0 0 0 10px rgba(225,6,0,0)
                }

                100% {
                    -moz-box-shadow: 0 0 0 0 rgba(225,6,0,0);
                    box-shadow: 0 0 0 0 rgba(225,6,0,0)
                }
            }

            .notification2 {
                width: 100%;
                float: left;
                padding: 10px 16px;
                border-bottom: solid .5px #e0e0e0;
                font-weight: 700
            }

            .lottery-today {
                text-align: center
            }

            .lottery-today a {
                font-family: sans-serif;
                float: left;
                width: 100%;
                color: #0029ad
            }

            .lottery-today td {
                height: 30px
            }

            .live-lottery {
                font-family: sans-serif;
                float: left;
                width: 100%;
                margin-bottom: 16px;
                padding: 7px;
                text-align: center;
                position: relative;
                background: bisque
            }

            .box-live {
                padding-bottom: 10px
            }

            .live-title {
                font-family: sans-serif;
                font-weight: bold
            }

            .live-box-title {
                font-size: 18px;
                text-align: center;
                font-weight: bold
            }

            .live-btn {
                font-family: sans-serif;
                cursor: pointer;
                background: #c80505;
                border-radius: 2px;
                color: #fff;
                padding: 2px 5px;
                font-size: 14px;
                display: inline-block;
                -webkit-animation: live-btn .7s infinite;
                -moz-animation: live-btn .7s infinite;
                -o-animation: live-btn .7s infinite;
                animation: live-btn .7s infinite;
                margin-left: 10px
            }

            .live-btn:hover {
                color: #fff
            }

            @-webkit-keyframes live-btn {
                50% {
                    background: #4285f4;
                    color: #fff
                }
            }

            .sms-loto a {
                text-decoration: underline
            }

            @media (max-width: 960px) {
                .live-lottery {
                    margin-bottom:12px;
                    padding: 0;
                    background: 0 0
                }
            }

            @media only screen and (min-width: 780px) {
                .advstickyleft {
                    position:fixed;
                    bottom: 8px;
                    right: calc(50% + 568px);
                    max-width: 200px;
                    z-index: 1000
                }

                .advstickyright {
                    position: fixed;
                    bottom: 8px;
                    left: calc(50% + 568px);
                    max-width: 200px;
                    z-index: 1000
                }

                .advfixfooter {
                    display: none
                }

                .advrightfooter {
                    max-width: 500px;
                    position: fixed;
                    right: 0;
                    bottom: 0
                }
            }

            @media only screen and (max-width: 779px) {
                .advstickyleft {
                    display:none
                }

                .advstickyright {
                    display: none
                }

                .advfixfooter {
                    position: fixed;
                    max-height: 120px;
                    width: 100%;
                    z-index: 1000;
                    left: 0;
                    bottom: 0;
                    text-align: center;
                    clear: both;
                    background: #fff
                }

                .advfixfooter .ads {
                    padding: 0 !important;
                    margin: 0 !important
                }

                .ads {
                    padding: 10px 0;
                    clear: both;
                    text-align: center
                }

                .advfixfooterClose {
                    position: absolute;
                    width: 30px;
                    height: 30px;
                    top: -30px;
                    right: 0;
                    padding: 3px;
                    z-index: 9999;
                    cursor: pointer;
                    background-size: 13px 13px;
                    background-position: 9px;
                    background-repeat: no-repeat;
                    box-shadow: 0 -1px 1px 0 rgba(0,0,0,.2);
                    border: none;
                    border-radius: 12px 0 0 0;
                    background: #f2f2f2
                }

                .advrightfooter {
                    display: none
                }
            }

            .notedelay {
                position: absolute;
                top: 68px;
                left: 0;
                animation: notedelay2 .7s 20;
                display: none;
                width: 100%;
                float: left;
                padding: 10px;
                background: #4caf50;
                text-align: center;
                color: #fff;
                font-weight: 700;
                font-size: 18px;
                border-radius: 5px;
                z-index: 1
            }

            .sms-loto span {
                font-size: 14px
            }

            @media (max-width: 800px) {
                .section-header h1 {
                    font-family:sans-serif;
                    font-size: 16px
                }

                .section-header h2 {
                    font-size: 18px
                }

                .site-link {
                    font-size: 13px
                }

                .site-link a+a::before {
                    padding: 0
                }

                .table-result th {
                    font-size: 14px
                }

                .table-loto th {
                    font-size: 14px
                }

                .btn-pushbar-3 {
                    left: 4px;
                    top: 4px;
                    width: 48px;
                    height: 48px;
                    line-height: 48px
                }

                .btn-calendar {
                    right: 4px;
                    top: 3px;
                    width: 48px;
                    height: 48px;
                    line-height: 48px
                }

                .notification {
                    font-size: 18px
                }

                .lottery-today {
                    font-size: 14px
                }

                .see-more a {
                    font-size: 14px
                }

                .btn-results {
                    font-size: 22px;
                    height: 40px;
                    width: 40px;
                    line-height: 40px
                }

                .code-DB1,.code-DB2,.code-DB3,.code-DB4,.code-DB5,.code-DB6,.code-DB7,.code-DB8 {
                    height: 36px;
                    line-height: 36px
                }

                .code-DB7 {
                    font-size: 18px
                }

                .code-DB8 {
                    font-size: 16px
                }

                .code-DB9 {
                    width: 20%;
                    font-size: 18px;
                    height: 30px;
                    line-height: 30px
                }

                .code-DB10 {
                    width: 20%;
                    font-size: 18px
                }

                .special-prize {
                    height: 36px;
                    line-height: 36px;
                    font-size: 32px
                }

                .prize1 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize2 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize3 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize4 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize5 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize6 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 24px
                }

                .prize7 {
                    height: 36px;
                    line-height: 36px;
                    font-size: 30px
                }

                .xs_prize1 {
                    height: 36px;
                    line-height: 36px
                }

                .xs_prize2 {
                    height: 36px;
                    line-height: 36px
                }

                .xs_prize3 {
                    height: 36px;
                    line-height: 36px
                }
            }

            @media only screen and (min-width: 961px) {
                .header-logo-img {
                    width:135px;
                    height: 48px
                }

                .header-content {
                    height: 58px
                }
            }

            @media (max-width: 414px) {
                .menu-item5 a {
                    font-size:12px
                }

                .xs_mn4 .runloto-0,.xs_mn4 .runloto-1,.xs_mn4 .runloto-2,.xs_mn4 .runloto-3,.xs_mn4 .runloto-4,.xs_mn4 .runloto-5,.xs_mn4 .runloto-6,.xs_mn4 .runloto-7,.xs_mn4 .runloto-8,.xs_mn4 .runloto-9 {
                    font-size: 15px;
                    padding: 0 2px
                }

                .xs_mn4 th {
                    width: 28px
                }

                .xs_mn4 td {
                    width: calc(25% - 7px)
                }

                .xs_mn4 span {
                    font-size: 21px
                }
            }

            .ketquamoi {
                background: #FF9;
                padding: 0 5px;
                border-radius: 3px;
                float: none !important;
                width: unset !important
            }

            .runloto-0,.runloto-1,.runloto-2,.runloto-3,.runloto-4,.runloto-5,.runloto-6,.runloto-7,.runloto-8,.runloto-9 {
                border-radius: 100%;
                color: #fff;
                padding: 0 3px;
                font-size: 22px
            }

            .runloto-0,.runloto-2,.runloto-4,.runloto-6,.runloto-8 {
                background: #333;
                background: -moz-linear-gradient(-45deg,#eb7164 0,#000);
                background: -webkit-gradient(left top,right bottom,color-stop(0,#333),color-stop(100%,#333));
                background: -webkit-linear-gradient(-45deg,#333 0,#333 100%);
                background: -o-linear-gradient(-45deg,#333 0,#333 100%);
                background: -ms-linear-gradient(-45deg,#333 0,#333 100%);
                background: linear-gradient(135deg,#333 0,#333 100%)
            }

            .runloto-1,.runloto-3,.runloto-5,.runloto-7,.runloto-9 {
                background: #b01014;
                background: -moz-linear-gradient(-45deg,#b01014 0,#b01014 100%);
                background: -webkit-gradient(left top,right bottom,color-stop(0,#b01014),color-stop(100%,#b01014));
                background: -webkit-linear-gradient(-45deg,#b01014 0,#b01014 100%);
                background: -o-linear-gradient(-45deg,#b01014 0,#b01014 100%);
                background: -ms-linear-gradient(-45deg,#b01014 0,#b01014 100%);
                background: linear-gradient(135deg,#b01014 0,#b01014 100%)
            }

            @-moz-keyframes notedelay2 {
                50% {
                    background: #ffec9f;
                    color: #fff
                }
            }

            @-o-keyframes notedelay2 {
                50% {
                    background: #ffec9f;
                    color: #fff
                }
            }

            @keyframes notedelay2 {
                50% {
                    background: #ffec9f;
                    color: #fff
                }
            }

            .keno-pad {
                padding: 16px 16px 0 16px
            }

            .keno-row {
                float: left;
                width: 100%;
                margin-bottom: 16px
            }

            .layout-grid-10 {
                display: grid;
                grid-column-gap: 5px;
                grid-row-gap: 5px;
                grid-template-columns: repeat(10,1fr);
                place-items: center
            }

            .btn-number-live {
                background: #fff;
                height: 44px;
                line-height: 44px;
                width: 44px;
                text-align: center;
                border-radius: 100%;
                border: solid 1px #c80505;
                color: #c80505;
                font-size: 24px;
                font-weight: bold;
                display: inline-block
            }

            .btn-number-live img {
                height: 14px
            }

            .keno-rowcl {
                float: left;
                width: 100%
            }

            .row-cl.fixclo2 {
                width: 23%;
                float: left;
                margin: 0 1%
            }

            .row-cl {
                background: #fff;
                display: block;
                line-height: 24px;
                margin: 2px 0;
                font-weight: bold;
                border-radius: 3px;
                border: solid 1px #c80505;
                padding: 4px 6px
            }

            .ic-cl {
                display: inline-block;
                color: #fff;
                width: 24px;
                height: 24px;
                text-align: center;
                line-height: 24px;
                border-radius: 100%;
                margin-right: 6px
            }

            .bg-chan {
                background: #1b66b9
            }

            .bg-le {
                background: #45ace7
            }

            .ic-btnkeno.keno-icLon {
                background: #f26531;
                position: relative
            }

            .ic-btnkeno.keno-icLon::after {
                position: relative;
                width: 24px;
                height: 24px;
                line-height: 24px;
                color: #FFF;
                text-align: center;
                border-radius: 50%;
                left: 0;
                content: ">";
                font-size: 16px
            }

            .ic-btnkeno.keno-icBe {
                background: #faa21e;
                position: relative
            }

            .ic-btnkeno.keno-icBe::after {
                position: relative;
                width: 24px;
                height: 24px;
                line-height: 24px;
                color: #FFF;
                text-align: center;
                border-radius: 50%;
                left: 0;
                content: "<";
                font-size: 16px
            }

            .red {
                color: #ed1c25
            }

            @media only screen and (max-width: 800px) {
                .layout-grid-10 {
                    grid-column-gap:3px;
                    grid-row-gap: 3px
                }

                .btn-number-live {
                    width: 8vw;
                    height: 8vw;
                    line-height: 8.3vw;
                    font-size: 5vw
                }

                .row-cl.fixclo2 {
                    width: 48%;
                    float: left;
                    margin: 0.5% 1%
                }
            }

            .headpn {
                height: 50px;
                width: 100%;
                float: left
            }

            .menu_ul li:hover > .menu_down {
                visibility: visible;
                opacity: 1
            }

            @media (hover: none) {
                .menu_ul li:hover > .menu_down {
                    visibility:hidden
                }
            }
        </style>
"""