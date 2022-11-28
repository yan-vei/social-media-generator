import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NewUser } from 'src/app/entities/user.model';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  token: string = 'user_token';
  errorMessage: string;

  profileForm = this.fb.group({
    username: [, Validators.required],
    password: [, Validators.required],
    email: [, Validators.required]
  });

  constructor(private router: Router, private auth: AuthService, private fb: FormBuilder) {
    window.onbeforeunload = function() {
      localStorage.clear();
      return '';
    };
  }

  ngOnInit()
  {
  }

  onRegister(): void {
    let user = new NewUser(this.profileForm.controls.username.value || '', this.profileForm.controls.password.value || '', this.profileForm.controls.email.value || '')
    this.auth.register(user)
    .subscribe((user) =>
    {
      localStorage.setItem(this.token, user['token']);
      this.router.navigate(['/generator']);
    },
    (err) =>
    {
      this.errorMessage = err.error['error'];
      console.log(err)
    }

    )
  }

}
