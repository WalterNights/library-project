import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-modal',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent {
@Input() show = false;
@Input() message = 'En unos segundos estará todo listo';
@Input() imgSrc = 'loading2.gif';
}