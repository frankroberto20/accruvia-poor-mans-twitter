import http from '../http-requests'

class TweetDataService {
    getAll() {
        return http.get("/tweets/")
    }
    create(data) {
        return http.post("/tweets/", data)
    }
}

export default new TweetDataService()