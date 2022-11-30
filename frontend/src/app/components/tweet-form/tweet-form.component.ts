import { Component, OnInit } from '@angular/core';
import { TweetService } from 'src/app/services/tweet.service';

@Component({
  selector: 'app-tweet-form',
  templateUrl: './tweet-form.component.html',
  styleUrls: ['./tweet-form.component.css']
})
export class TweetFormComponent implements OnInit {
  public tweet: any;
  public hashtags: any[];

  public tweetText: string;
  public hashtag: string = "";
  public selectedHts: number = 0;

  constructor(public tweetService: TweetService) {
  }

  ngOnInit(): void {
    this.tweet = this.tweetService.selectedTweet;
    this.hashtags = this.tweetService.selectedHashtags;
    this.tweetText = this.tweetService.selectedTweet['post'];
  }

  getTweetUrl(): string {
    let text = this.tweetText;
    let hashtags = this.hashtag.slice(0, this.hashtag.length - 1)
    return "https://twitter.com/intent/tweet?text=" + text +"&hashtags=" + hashtags;
  }

  getHashtag(index: number) {
    return Object.keys(this.hashtags[index])[0]
  }

  getTotalCharacterCount() {
    let ht = this.hashtag.slice(0, this.hashtag.length -1);
    let totalCount = this.tweetText.length + ht.length + this.selectedHts;
    const characterCount = document.getElementById('characterCount')!;
    if (totalCount > 280) {
      characterCount.style.color = "red";
    }
    else {
      characterCount.style.color = "darkblue";
    }
    return totalCount;
  }

  addToSelected(div: any) {
    const ht = document.getElementById(div.id)!;
    ht.style.border = "1px solid black";
    let htText = ht.innerText.slice(1);
    this.hashtag += htText + ',';
    this.selectedHts++;
  }

}
