<template>
  <div class="container">
    <div class="row">
      <h4>Tweets</h4>
        <div v-for="(tweet, index) in tweets"
          :key="index"> 
          <article class="border-bottom p-2">
            <span class="float-right"><em>{{tweet.timestamp}}</em></span>
            <span><strong class="ml-3">{{tweet.name}}</strong></span>
            <p class="m-3" style="white-space: pre-line;">
              {{tweet.text}}
            </p>
          </article>
        </div>
    </div>
  </div>
</template>

<script>
import TweetDataService from '../services/TweetDataService';

export default {
  name: "TweetList",
  data() {
    return {
      tweets: []
    };
  },
  methods: {
    retrieveTweets() {
      TweetDataService.getAll()
        .then(response => {
          this.tweets = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveTweets();
    },
    
  },
  mounted() {
    this.retrieveTweets();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>