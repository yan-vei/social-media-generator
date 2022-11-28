import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LogoutService } from 'src/app/services/logout.service';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private router: Router, public logout: LogoutService) { }

  ngOnInit(): void {
    if (localStorage.getItem('user_token'))
    {
      this.router.navigate(['/generator'])
    }
  }

}
