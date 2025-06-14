import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { ModalComponent } from '../../shared/modal/modal.component';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalComponent],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  credentials = { username: '', password: '' };
  error = '';

  showModal = false;

  constructor(private http: HttpClient, private router: Router) { }

  login() {
    this.http.post<any>(`${environment.apiUrl}/token/`, this.credentials).subscribe({
      next: res => {
        localStorage.setItem('access_token', res.access);
        this.showModal = true;
        this.http.get<any>(`${environment.apiUrl}/users/me/`, {
          headers: { Authorization: `Bearer ${res.access}` }
        }).subscribe(user => {
          localStorage.setItem('user_id', user.id);
          localStorage.setItem('user', JSON.stringify(user));
          setTimeout(() => {
            this.showModal = false;
            this.router.navigate(['/']);
          }, 3000);
        });
      },
      error: () => {
        this.error = 'Usuario o contraseña incorrectos';
      }
    });
  }

  goToRegister() {
    this.router.navigate(['/auth/register']);
  }
}