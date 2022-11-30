import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TweetService {
  public selectedTweet: any;
  public selectedHashtags: any[] = [];

  constructor() { }
}
