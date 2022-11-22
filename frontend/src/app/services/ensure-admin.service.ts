import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { map, catchError } from "rxjs/operators";
import { API_URL } from '../env';


@Injectable()
export class EnsureAdmin implements CanActivate {
  private url: string = `${API_URL}/admin`
  private userToken: string = localStorage.getItem("user_token") || '';
  private headers: HttpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': this.userToken});

  constructor(private router: Router, private http: HttpClient) {}

  canActivate(): Observable<boolean>{
    return this.http.get(this.url, {headers: this.headers}).pipe(
      map((e) => {
        return true
      }),
      catchError((err) => {
        this.router.navigate(['/login'])
        return of(false)
      })
    )
}

}
