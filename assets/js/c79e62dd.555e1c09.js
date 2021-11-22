"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[8555],{3905:function(e,t,a){a.d(t,{Zo:function(){return m},kt:function(){return u}});var r=a(7294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,r,n=function(e,t){if(null==e)return{};var a,r,n={},i=Object.keys(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var p=r.createContext({}),s=function(e){var t=r.useContext(p),a=t;return e&&(a="function"==typeof e?e(t):l(l({},t),e)),a},m=function(e){var t=s(e.components);return r.createElement(p.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var a=e.components,n=e.mdxType,i=e.originalType,p=e.parentName,m=o(e,["components","mdxType","originalType","parentName"]),d=s(a),u=n,y=d["".concat(p,".").concat(u)]||d[u]||c[u]||i;return a?r.createElement(y,l(l({ref:t},m),{},{components:a})):r.createElement(y,l({ref:t},m))}));function u(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=a.length,l=new Array(i);l[0]=d;var o={};for(var p in t)hasOwnProperty.call(t,p)&&(o[p]=t[p]);o.originalType=e,o.mdxType="string"==typeof e?e:n,l[1]=o;for(var s=2;s<i;s++)l[s]=a[s];return r.createElement.apply(null,l)}return r.createElement.apply(null,a)}d.displayName="MDXCreateElement"},5599:function(e,t,a){a.r(t),a.d(t,{frontMatter:function(){return o},contentTitle:function(){return p},metadata:function(){return s},toc:function(){return m},default:function(){return d}});var r=a(7462),n=a(3366),i=(a(7294),a(3905)),l=["components"],o={"sidebar position":3},p=void 0,s={unversionedId:"mapillary.models/mapillary.models.exceptions",id:"mapillary.models/mapillary.models.exceptions",isDocsHomePage:!1,title:"mapillary.models.exceptions",description:"mapillary.models.exceptions",source:"@site/docs/mapillary.models/mapillary.models.exceptions.md",sourceDirName:"mapillary.models",slug:"/mapillary.models/mapillary.models.exceptions",permalink:"/mapillary-python-sdk/docs/mapillary.models/mapillary.models.exceptions",editUrl:"https://github.com/mapillary/mapillary-python-sdk/tree/main/docs/docs/mapillary.models/mapillary.models.exceptions.md",tags:[],version:"current",frontMatter:{"sidebar position":3},sidebar:"tutorialSidebar",previous:{title:"mapillary.models.client",permalink:"/mapillary-python-sdk/docs/mapillary.models/mapillary.models.client"},next:{title:"mapillary.models.geojson",permalink:"/mapillary-python-sdk/docs/mapillary.models/mapillary.models.geojson"}},m=[{value:"mapillary.models.exceptions",id:"mapillarymodelsexceptions",children:[]},{value:"exception mapillary.models.exceptions.AuthError(message: str)",id:"exception-mapillarymodelsexceptionsautherrormessage-str",children:[]},{value:"exception mapillary.models.exceptions.InvalidFieldError(endpoint: str, field: list)",id:"exception-mapillarymodelsexceptionsinvalidfielderrorendpoint-str-field-list",children:[]},{value:"exception mapillary.models.exceptions.InvalidImageKeyError(image_id: Unionint, str)",id:"exception-mapillarymodelsexceptionsinvalidimagekeyerrorimage_id-unionint-str",children:[]},{value:"exception mapillary.models.exceptions.InvalidImageResolutionError(resolution: int)",id:"exception-mapillarymodelsexceptionsinvalidimageresolutionerrorresolution-int",children:[]},{value:"exception mapillary.models.exceptions.InvalidKwargError(func: str, key: str, value: str, options: list)",id:"exception-mapillarymodelsexceptionsinvalidkwargerrorfunc-str-key-str-value-str-options-list",children:[]},{value:"exception mapillary.models.exceptions.InvalidOptionError(param: str, value: any, options: list)",id:"exception-mapillarymodelsexceptionsinvalidoptionerrorparam-str-value-any-options-list",children:[]},{value:"exception mapillary.models.exceptions.InvalidTokenError(message: str, error_type: str, code: str, fbtrace_id: str)",id:"exception-mapillarymodelsexceptionsinvalidtokenerrormessage-str-error_type-str-code-str-fbtrace_id-str",children:[]},{value:"exception mapillary.models.exceptions.MapillaryException()",id:"exception-mapillarymodelsexceptionsmapillaryexception",children:[]}],c={toc:m};function d(e){var t=e.components,a=(0,n.Z)(e,l);return(0,i.kt)("wrapper",(0,r.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h3",{id:"mapillarymodelsexceptions"},"mapillary.models.exceptions"),(0,i.kt)("p",null,"This module contains the set of Mapillary Exceptions used internally."),(0,i.kt)("p",null,"For more information, please check out ",(0,i.kt)("a",{parentName:"p",href:"https://www.mapillary.com/developer/api-documentation/"},"https://www.mapillary.com/developer/api-documentation/"),"."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Copyright: (c) 2021 Facebook")),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"License: MIT LICENSE")),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsautherrormessage-str"},"exception mapillary.models.exceptions.AuthError(message: str)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when a function is called without having the access token set in\nset_access_token to access Mapillary\u2019s API, primarily used in mapillary.set_access_token"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"message")," \u2013 The error message returned"))),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidfielderrorendpoint-str-field-list"},"exception mapillary.models.exceptions.InvalidFieldError(endpoint: str, field: list)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when an API endpoint is passed invalid field elements"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"endpoint")," \u2013 The API endpoint that was targeted")))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"* **field** \u2013 The invalid field that was passed\n")),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidimagekeyerrorimage_id-unionint-str"},"exception mapillary.models.exceptions.InvalidImageKeyError(image_id: Union","[int, str]",")"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when trying to retrieve an image thumbnail with an invalid image ID/key.\nPrimarily used with mapillary.image_thumbnail"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"image_id")," \u2013 Image ID/key entered by the user"))),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Parameters")),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"image_id")," \u2013 int"))),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidimageresolutionerrorresolution-int"},"exception mapillary.models.exceptions.InvalidImageResolutionError(resolution: int)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when trying to retrieve an image thumbnail with an invalid resolution/size."),(0,i.kt)("p",null,"Primarily used with mapillary.image_thumbnail"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"resolution")," \u2013 Image size entered by the user"))),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidkwargerrorfunc-str-key-str-value-str-options-list"},"exception mapillary.models.exceptions.InvalidKwargError(func: str, key: str, value: str, options: list)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when a function is called with the invalid keyword argument(s) that do not belong to the\nrequested API end call"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"func")," \u2013 The function that was called")))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"* **key** \u2013 The key that was passed\n\n\n* **value** \u2013 The value along with that key\n\n\n* **options** \u2013 List of possible keys that can be passed\n")),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidoptionerrorparam-str-value-any-options-list"},"exception mapillary.models.exceptions.InvalidOptionError(param: str, value: any, options: list)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Out of bound zoom error"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"param")," \u2013 The invalid param passed")))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"* **value** \u2013 The invalid value passed\n\n\n* **options** \u2013 The possible list of zoom values\n")),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsinvalidtokenerrormessage-str-error_type-str-code-str-fbtrace_id-str"},"exception mapillary.models.exceptions.InvalidTokenError(message: str, error_type: str, code: str, fbtrace_id: str)"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"mapillary.models.exceptions.MapillaryException")),(0,i.kt)("p",null,"Raised when an invalid token is given\nto access Mapillary\u2019s API, primarily used in mapillary.set_access_token"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("strong",{parentName:"p"},"Variables")),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"message")," \u2013 The error message returned")))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"* **error_type** \u2013 The type of error that occurred\n\n\n* **code** \u2013 The error code returned, most likely 190, \u201cAccess token has expired\u201d.\nSee [https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/](https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/)\nfor more information\n\n\n* **fbtrace_id** \u2013 A unique ID to track the issue/exception\n")),(0,i.kt)("h3",{id:"exception-mapillarymodelsexceptionsmapillaryexception"},"exception mapillary.models.exceptions.MapillaryException()"),(0,i.kt)("p",null,"Bases: ",(0,i.kt)("inlineCode",{parentName:"p"},"Exception")),(0,i.kt)("p",null,"Base class for exceptions in this module"))}d.isMDXComponent=!0}}]);