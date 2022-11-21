import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { RequestDataUrl } from 'src/app/entities/request-data.model';
import { GeneratorService } from 'src/app/services/generator.service';

@Component({
  selector: 'generator',
  templateUrl: './generator.component.html',
  styleUrls: ['./generator.component.css']
})
export class GeneratorComponent implements OnInit {
  urlForm = this.fb.group({
    url: [, Validators.required]
  });

  constructor(private generatorService: GeneratorService, private fb: FormBuilder) { }

  ngOnInit(): void {
  }

  generateTweets()
  {
    let data = new RequestDataUrl(this.urlForm.controls.url.value || '')
    this.generatorService.generateTweetsFromUrl(data)
    .subscribe((tweets) =>
    console.log(tweets)
    )
  }
}
