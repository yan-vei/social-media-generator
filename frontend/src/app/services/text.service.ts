import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

import {API_URL} from '../env';
import {TextExtract} from '../entities/text-extract.model';
import { Post } from '../entities/post.model';

@Injectable()
export class TextService {
  private userToken: string = localStorage.getItem("user_token") || '';
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': this.userToken});


  constructor(private http: HttpClient) {
  }

  getTextExtracts(): Observable<TextExtract[]> {
    let url: string = `${API_URL}/text-extracts`
    return this.http.get<TextExtract[]>(url, {headers: this.headers});
  }

  getTextExtractsPosts(id: number): Observable<Post[]> {
    let url: string = `${API_URL}/posts-by-text-extract?id=${id}`
    return this.http.get<Post[]>(url, {headers: this.headers});
  }
}
