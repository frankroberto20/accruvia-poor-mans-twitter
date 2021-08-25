import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/tweets",
    name: "tweets",
    component: () => import("./components/TweetList")
  },
  {
    path: "/post",
    name: "post",
    component: () => import("./components/TweetForm")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;