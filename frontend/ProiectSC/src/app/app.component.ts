import { Component } from '@angular/core';
import { RsaService } from 'src/services/rsa.service';
import { Rc4Service } from 'src/services/rc4.service';
import { AesService } from 'src/services/aes.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private rsaService:RsaService,private rc4Service:Rc4Service, private aesService:AesService){}
  title = 'ProiectSC';
  toEncryptRSA:string|undefined
  encryptedRSA:string=""
  toDecryptRSA:string=""
  decryptedRSA:string=""

  RC4key:string=""
  toEncryptRC4:string=""
  encryptedRC4:string=""
  toDecryptRC4:string=""
  decryptedRC4:string=""

  AESkey:string=""
  toEncryptAES:string=""
  encryptedAES:string=""
  toDecryptAES:string=""
  decryptedAES:string=""

  RSAEncrypt(){
    this.rsaService.RSAEncrypt({'message':this.toEncryptRSA!}).subscribe(result=>this.encryptedRSA=result)
  }

  RSADecrypt(){
    this.rsaService.RSADecrypt({'message':this.toDecryptRSA!}).subscribe(result=>this.decryptedRSA=result)
  }

  RC4Encrypt(){
    this.rc4Service.RC4Encrypt({'message':this.toEncryptRC4!,'key':this.RC4key}).subscribe(result=>this.encryptedRC4=result)
  }

  RC4Decrypt(){
    this.rc4Service.RC4Decrypt({'message':this.toDecryptRC4!,'key':this.RC4key}).subscribe(result=>this.decryptedRC4=result)
  }

  AESEncrypt(){
    this.aesService.AESEncrypt({'message':this.toEncryptAES!,'key':this.AESkey}).subscribe(result=>this.encryptedAES=result)
  }

  AESDecrypt(){
    this.aesService.AESDecrypt({'message':this.toDecryptAES!,'key':this.AESkey}).subscribe(result=>this.decryptedAES=result)
  }
}