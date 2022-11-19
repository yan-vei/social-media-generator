import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { User } from '../../entities/user.model';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  profileForm = this.fb.group({
    username: [, Validators.required],
    email: [, Validators.required],
    password: [, Validators.required]
  });

  constructor(private router: Router, private auth: AuthService, private fb: FormBuilder) {}

  onSubmit(): void {
    let user = new User(this.profileForm.controls.username.value || '', this.profileForm.controls.email.value || '', this.profileForm.controls.password.value || '')
    this.auth.login(user)
    .subscribe((user) =>
    {
      console.log(user);
    })
  }
}
