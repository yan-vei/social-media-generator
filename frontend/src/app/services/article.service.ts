import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';

import {API_URL} from '../env';
import {Article} from '../entities/article.model';
import { Post } from '../entities/post.model';

@Injectable()
export class ArticleService {
  private userToken: string = localStorage.getItem("user_token") || '';
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': this.userToken});

  constructor(private http: HttpClient) {
  }

  getAllArticles(): Observable<Article[]> {
    let url: string = `${API_URL}/all-articles`
    return this.http.get<Article[]>(url, {headers: this.headers});
  }

  getArticles(): Observable<Article[]> {
    let url: string = `${API_URL}/articles`
    return this.http.get<Article[]>(url, {headers: this.headers});
  }

  getArticlePosts(id: number): Observable<Post[]>
  {
    let url: string = `${API_URL}/posts-by-article?id=${id}`
    return this.http.get<Post[]>(url, {headers: this.headers});
  }

  deleteArticle(id: number): Observable<any> {
    let url: string = `${API_URL}/articles?id=${id}`
    return this.http.delete(url)
  }

}
