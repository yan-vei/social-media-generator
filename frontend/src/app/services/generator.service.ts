import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Post } from '../entities/post.model';
import { RequestDataText, RequestDataUrl } from '../entities/request-data.model';
import {API_URL} from '../env';

@Injectable({
  providedIn: 'root'
})
export class GeneratorService {

  constructor(private http: HttpClient) { }

  generateTweetsFromUrl(data: RequestDataUrl, userToken: string): Observable<any> {
    let httpHeaders: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/posts`;
    return this.http.post(url, data, {headers: httpHeaders});
  }

  generateTweetsFromText(data: RequestDataText, userToken: string): Observable<any> {
    let httpHeaders: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': userToken});
    let url: string = `${API_URL}/posts`;
    return this.http.post(url, data, {headers: httpHeaders});
  }
}
