import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { RequestDataText, RequestDataUrl } from 'src/app/entities/request-data.model';
import { GeneratorService } from 'src/app/services/generator.service';
import {Post} from 'src/app/entities/post.model'
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'generator',
  templateUrl: './generator.component.html',
  styleUrls: ['./generator.component.css']
})
export class GeneratorComponent implements OnInit {
  public generatedTweets: any = null;
  public generatedHashtags: any = null;

  urlForm = this.fb.group({
    url: [, Validators.required]
  });

  textForm = this.fb.group({
    title: [, Validators.required],
    text: [, Validators.required],
    source: [, Validators.required]
  });

  constructor(private generatorService: GeneratorService, private fb: FormBuilder, private utilsService: UtilsService) { }

  ngOnInit(): void {
  }

  generateTweets()
  {
    if (this.urlForm.valid)
    {
      let data = new RequestDataUrl(this.urlForm.controls.url.value || '')
      this.generatorService.generateTweetsFromUrl(data)
      .subscribe((tweets) =>
      {
        this.generatedTweets = tweets['tweets'].splice(1, tweets['tweets'].length-1)
        this.generatedTweets.sort(this.utilsService.compare)
        this.generatedHashtags = tweets['hashtags'].splice(1, tweets['hashtags'].length-1)
      }


      )
    }

    else if (this.textForm.valid)
    {
      let data = new RequestDataText(this.textForm.controls.text.value || '', this.textForm.controls.text.value || '', this.textForm.controls.source.value || '')
      this.generatorService.generateTweetsFromText(data)
      .subscribe((tweets) =>
      {
        this.generatedTweets = tweets['tweets'].splice(1, tweets['tweets'].length-1)
        this.generatedTweets.sort(this.utilsService.compare)
        this.generatedHashtags = tweets['hashtags'].splice(1, tweets['hashtags'].length-1)
      }

      )
    }
  }

}
