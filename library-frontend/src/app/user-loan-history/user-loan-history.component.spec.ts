import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserLoanHistoryComponent } from './user-loan-history.component';

describe('UserLoanHistoryComponent', () => {
  let component: UserLoanHistoryComponent;
  let fixture: ComponentFixture<UserLoanHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserLoanHistoryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UserLoanHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
