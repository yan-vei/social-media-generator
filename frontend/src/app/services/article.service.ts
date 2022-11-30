import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';

import {API_URL} from '../env';
import {Article} from '../entities/article.model';
import { Post } from '../entities/post.model';

@Injectable()
export class ArticleService {

  constructor(private http: HttpClient) {
  }

  getAllArticles(): Observable<Article[]> {
    let userToken: string = localStorage.getItem("user_token") || '';
    let headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/all-articles`
    return this.http.get<Article[]>(url, {headers: headers});
  }

  getArticles(): Observable<Article[]> {
    let userToken: string = localStorage.getItem("user_token") || '';
    let headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/articles`
    return this.http.get<Article[]>(url, {headers: headers});
  }

  getArticlePosts(id: number): Observable<Post[]>
  {
    let userToken: string = localStorage.getItem("user_token") || '';
    let headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/posts-by-article?id=${id}`
    return this.http.get<Post[]>(url, {headers: headers});
  }

  deleteArticle(id: number): Observable<any> {
    let url: string = `${API_URL}/articles?id=${id}`
    return this.http.delete(url)
  }

  getArticleByTitle(title: string): Observable<any>
  {
    let userToken: string = localStorage.getItem("user_token") || '';
    let headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/articles-by-title?title=${title}`
    return this.http.get(url, {headers: headers})
  }

}
