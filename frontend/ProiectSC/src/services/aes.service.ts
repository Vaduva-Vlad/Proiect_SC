import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AesService {

  constructor(private http:HttpClient) { }

  AESEncrypt(data:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/encrypt/aes",data)
  }

  AESDecrypt(data:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/decrypt/aes",data)
  }
}
