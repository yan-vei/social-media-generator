import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

import {API_URL} from '../env';
import {Article} from '../entities/article.model';

@Injectable()
export class ArticleApiService {

  constructor(private http: HttpClient) {
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(`${API_URL}/articles`);
  }
}
