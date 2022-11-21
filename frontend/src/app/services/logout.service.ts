import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class LogoutService {

  constructor(private auth: AuthService) { }

  onLogout(): void {
    this.auth.logout()
    .subscribe((user) =>
    {
      localStorage.removeItem('user_token');
    },
    err =>
    {
      console.log(err);
    })
  }
}
