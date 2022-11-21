import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class LogoutService {

  constructor(private router: Router, private auth: AuthService) { }

  onLogout(): void {
    this.auth.logout()
    .subscribe((user) =>
    {
      localStorage.removeItem('user_token');
      this.router.navigate(['/'])
    },
    err =>
    {
      console.log(err);
    })
  }
}
