import { Injectable } from '@angular/core';
import { Post } from '../entities/post.model';

@Injectable({
  providedIn: 'root'
})
export class UtilsService {

  constructor() { }

  compare(a: Post, b: Post)
  {
    let comparison = 0;
    if (a.score > b.score) {
      comparison = -1;
    } else if (a.score< b.score) {
      comparison = 1;
    }
    return comparison;
  }

  isLoggedIn() {
    return localStorage.getItem('user_token');
  }
}
