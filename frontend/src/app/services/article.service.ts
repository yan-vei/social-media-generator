import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

import {API_URL} from '../env';
import {Article} from '../entities/article.model';

@Injectable()
export class ArticleService {
  private userToken: string = localStorage.getItem("user_token") || '';
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': this.userToken});

  constructor(private http: HttpClient) {
  }

  getArticles(): Observable<Article[]> {
    let url: string = `${API_URL}/articles`
    return this.http.get<Article[]>(url, {headers: this.headers});
  }
}
