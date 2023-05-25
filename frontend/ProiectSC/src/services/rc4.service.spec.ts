import { TestBed } from '@angular/core/testing';

import { Rc4Service } from './rc4.service';

describe('Rc4Service', () => {
  let service: Rc4Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Rc4Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
