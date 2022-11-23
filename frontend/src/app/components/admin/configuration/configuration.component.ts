import { Component, OnInit } from '@angular/core';
import { AdminService } from 'src/app/services/admin.service';

@Component({
  selector: 'configuration',
  templateUrl: './configuration.component.html',
  styleUrls: ['./configuration.component.css']
})
export class ConfigurationComponent implements OnInit {
  private file: File;

  constructor(public adminService: AdminService) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any)
  {
    this.file = event.target.files[0];
    console.log(this.file)
  }

  uploadFile() {
    console.log(this.file)
    this.adminService.uploadFile(this.file).subscribe((data) => console.log(data))
  }

}
