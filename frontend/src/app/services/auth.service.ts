import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {API_URL} from '../env';
import { Observable } from 'rxjs';
import { User } from '../entities/user.model';

@Injectable()
export class AuthService {
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) {}

  login(user: User): Observable<any> {
    let url: string = `${API_URL}/users/login`;
    return this.http.post(url, user, {headers: this.headers});
  }

  logout(userToken: string): Observable<any> {
    let url: string = `${API_URL}/users/logout`;
    return this.http.get(url);
  }

  register(user: User): Observable<any> {
    let url: string = `${API_URL}/users/register`;
    return this.http.post(url, user, {headers: this.headers});
  }
}
