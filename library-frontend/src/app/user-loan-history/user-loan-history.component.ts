import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-user-loan-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './user-loan-history.component.html',
  styleUrls: ['./user-loan-history.component.css']
})
export class UserLoanHistoryComponent implements OnInit {
history: any[] = [];
loading = true;
error = '';

constructor(private http: HttpClient) {}

ngOnInit(): void {
  const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
  this.http.get<any[]>(`${environment.apiUrl}/users/me/history/`, {
    headers: { Authorization: `Bearer ${token}` }
  }).subscribe({
    next: data => {
      this.history = data;
      this.loading = false;
    },
    error: (err) => {
      this.error = 'No se pudo cargar el historial de préstamos';
      this.loading = false;
    }
  })
}

}
