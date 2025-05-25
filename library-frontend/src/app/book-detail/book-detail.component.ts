import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.css'],
})
export class BookDetailComponent implements OnInit {
  book: any;
  user: any;
  hasBook = false;

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute,
    private router: Router,
  ) { }

  ngOnInit(): void {
    const bookId = this.route.snapshot.paramMap.get('id');
    this.http.get(`${environment.apiUrl}/books/${bookId}/`).subscribe(book => {
      this.book = book;
    });

    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return;
    }

    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (!token) {
      this.router.navigate(['/auth/login']);
      return;
    }

    this.http.get(`${environment.apiUrl}/users/me/`, {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe({
      next: (user: any) => {
        this.user = user;
        this.hasBook = user.borrowed_book.includes(Number(bookId));
      },
      error: (err) => {
        if (err.status === 401) {
          localStorage.removeItem('access_token');
          this.router.navigate(['/auth/login']);
        }
      }
    });
  }

  onImgErr(event: Event) {
    (event.target as HTMLImageElement).src = 'book-placeholder.png';
  }

  lend_book() {
    const token = localStorage.getItem('access_token');
    this.http.post(`${environment.apiUrl}/books/${this.book.id}/lend/`, {},
      {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(() => {
        this.hasBook = true;
      });
  }

  return_book() {
    const token = localStorage.getItem('access_token');
    this.http.post(`${environment.apiUrl}/books/${this.book.id}/return/`, {},
      {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(() => {
        this.hasBook = false;
      });
  }
}
