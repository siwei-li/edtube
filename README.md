# EdTube

> A Vue.js + Django video platform

![logo_200x200](https://i.loli.net/2020/12/23/jUCBcufs2H4bgZY.png)

## Frontend Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```



## Tech Stack

选择了 VueJS 的前端渲染，放弃了 Django 的后端模板引擎渲染，业务逻辑放到了前端，放弃了 Django 的 View。

保留了 Django 的 Controller (URLconf) 来实现前端路由的父级路由，可以达到不同页面使用不同的前端框架， 页面内部使用各自独有的前端路由的效果。

保留了 Django 的 Model ，配合 Django Admin使用 Django ORM 。

```
M(Django) + C(Django) + MVVM (VueJS) = M + MVVM + C = MMVVMC
```



项目组织包括client_side文件夹和server_api文件夹：前者是vue单页面应用项目，它提供一个入口页面，页面中有一系列取数和数据组织逻辑。后者是一个Django项目，它管理数据库和api行为。



Axios to send AJAX requests to the Django backend.



## Auth0 Authentication

Uses Auth0 to implement user authentivation.

