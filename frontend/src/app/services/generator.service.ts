import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RequestDataUrl } from '../entities/request-data.model';
import {API_URL} from '../env';

@Injectable({
  providedIn: 'root'
})
export class GeneratorService {
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  generateTweetsFromUrl(data: RequestDataUrl): Observable<any> {
    let url: string = `${API_URL}/posts`;
    return this.http.post(url, data, {headers: this.headers});
  }
}