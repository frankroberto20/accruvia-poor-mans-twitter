<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="name">Name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="tweet.name"
          name="name"
        />
      </div>

      <div class="form-group">
        <label for="text">Text</label>
        <textarea
          rows="2"
          maxlength="50"
          class="form-control"
          id="text"
          required
          v-model="tweet.text"
          name="text"
        />
      </div>

      <button @click="saveTweet" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newTweet">Post</button>
    </div>
  </div>
</template>

<script>
import TweetDataService from "../services/TweetDataService";

export default {
  name: "TweetForm",
  data() {
    return {
      tweet: {
        name: "",
        text: "",
      },
      submitted: false
    };
  },
  methods: {
    saveTweet() {
      var data = {
        name: this.tweet.name,
        text: this.tweet.text
      };

      TweetDataService.create(data)
        .then(response => {
          this.tweet.id = response.data.id;
          this.tweet.timestamp = response.data.timestamp
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newTweet() {
      this.submitted = false;
      this.tweet = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 600px;
  margin: auto;
}
</style>