import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BulkUploadBooksComponent } from './bulk-upload-books.component';

describe('BulkUploadBooksComponent', () => {
  let component: BulkUploadBooksComponent;
  let fixture: ComponentFixture<BulkUploadBooksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BulkUploadBooksComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BulkUploadBooksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
