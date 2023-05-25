import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RsaService {

  constructor(private http:HttpClient) { }


  RSAEncrypt(message:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/encrypt/rsa",message)
  }

  RSADecrypt(message:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/decrypt/rsa",message)
  }
}
