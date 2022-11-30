import { Component, OnInit } from '@angular/core';
import { TweetService } from 'src/app/services/tweet.service';

@Component({
  selector: 'app-tweet-form',
  templateUrl: './tweet-form.component.html',
  styleUrls: ['./tweet-form.component.css']
})
export class TweetFormComponent implements OnInit {
  public tweet: any;
  public hashtags: any[]

  constructor(public tweetService: TweetService) { }

  ngOnInit(): void {
    this.tweet = this.tweetService.selectedTweet;
    this.hashtags = this.tweetService.selectedHashtags;
  }

  getTweetUrl(): string {
    let text = this.tweet.post;
    return "https://twitter.com/intent/tweet?text=" + text;
  }

}
