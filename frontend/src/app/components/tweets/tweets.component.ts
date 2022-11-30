import { NONE_TYPE } from '@angular/compiler';
import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TweetService } from 'src/app/services/tweet.service';
import { GeneratorComponent } from '../generator/generator.component';

@Component({
  selector: 'tweets',
  templateUrl: './tweets.component.html',
  styleUrls: ['./tweets.component.css']
})
export class TweetsComponent implements OnInit {
  @Input() generatedTweets: any;
  @Input() generatedHashtags: any;

  constructor(private router: Router, private tweetService: TweetService) { }

  ngOnInit(): void {

  }

  getHashtag(index: number) {
    return Object.keys(this.generatedHashtags[index])[0]
  }

  getHashtagScore(index: number) {
    return this.generatedHashtags[index][Object.keys(this.generatedHashtags[index])[0]]
  }

 getSelectedTweet(index: number): void {
    this.tweetService.selectedTweet = this.generatedTweets[index];
    this.router.navigate(['/tweet'])
  }

  getSelectedHashtag(div: any, index: number) {
    let flag: boolean = false;
    const ht = document.getElementById(div.id)!;
    console.log(div)
    ht.style.border = "1px solid black";
    for (let i = 0; i < this.tweetService.selectedHashtags.length; i++) {
      if (this.generatedHashtags[index] === this.tweetService.selectedHashtags[i]) {
        flag = true;
      }
    }
    if (!flag)
    {
      this.tweetService.selectedHashtags.push(this.generatedHashtags[index]);
    }
  }
}
