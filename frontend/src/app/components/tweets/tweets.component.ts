import { Component, Input, OnInit } from '@angular/core';
import { Post } from 'src/app/entities/post.model';

@Component({
  selector: 'tweets',
  templateUrl: './tweets.component.html',
  styleUrls: ['./tweets.component.css']
})
export class TweetsComponent implements OnInit {
  @Input() generatedTweets: any;
  @Input() generatedHashtags: any;

  constructor() { }

  ngOnInit(): void {

  }

  getHashtag(index: number) {
    return Object.keys(this.generatedHashtags[index])[0]
  }

  getHashtagScore(index: number) {
    return this.generatedHashtags[index][Object.keys(this.generatedHashtags[index])[0]]
  }

}
