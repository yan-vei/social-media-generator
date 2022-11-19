import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import {API_URL} from '../env';
import {Article} from '../entities/article.model';

@Injectable()
export class ArticleApiService {

  constructor(private http: HttpClient) {
  }

  // GET list of public, future events
  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(`${API_URL}/articles`);
  }
}
