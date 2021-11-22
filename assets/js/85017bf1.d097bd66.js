"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[654],{3905:function(e,t,a){a.d(t,{Zo:function(){return f},kt:function(){return u}});var i=a(7294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,i)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,i,n=function(e,t){if(null==e)return{};var a,i,n={},r=Object.keys(e);for(i=0;i<r.length;i++)a=r[i],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(i=0;i<r.length;i++)a=r[i],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var p=i.createContext({}),c=function(e){var t=i.useContext(p),a=t;return e&&(a="function"==typeof e?e(t):l(l({},t),e)),a},f=function(e){var t=c(e.components);return i.createElement(p.Provider,{value:t},e.children)},s={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},m=i.forwardRef((function(e,t){var a=e.components,n=e.mdxType,r=e.originalType,p=e.parentName,f=o(e,["components","mdxType","originalType","parentName"]),m=c(a),u=n,g=m["".concat(p,".").concat(u)]||m[u]||s[u]||r;return a?i.createElement(g,l(l({ref:t},f),{},{components:a})):i.createElement(g,l({ref:t},f))}));function u(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var r=a.length,l=new Array(r);l[0]=m;var o={};for(var p in t)hasOwnProperty.call(t,p)&&(o[p]=t[p]);o.originalType=e,o.mdxType="string"==typeof e?e:n,l[1]=o;for(var c=2;c<r;c++)l[c]=a[c];return i.createElement.apply(null,l)}return i.createElement.apply(null,a)}m.displayName="MDXCreateElement"},7258:function(e,t,a){a.r(t),a.d(t,{frontMatter:function(){return o},contentTitle:function(){return p},metadata:function(){return c},toc:function(){return f},default:function(){return m}});var i=a(7462),n=a(3366),r=(a(7294),a(3905)),l=["components"],o={"sidebar position":3},p=void 0,c={unversionedId:"mapillary.config.api/mapillary.config.api.general",id:"mapillary.config.api/mapillary.config.api.general",isDocsHomePage:!1,title:"mapillary.config.api.general",description:"mapillary.config.api.general",source:"@site/docs/mapillary.config.api/mapillary.config.api.general.md",sourceDirName:"mapillary.config.api",slug:"/mapillary.config.api/mapillary.config.api.general",permalink:"/mapillary-python-sdk/docs/mapillary.config.api/mapillary.config.api.general",editUrl:"https://github.com/mapillary/mapillary-python-sdk/tree/main/docs/docs/mapillary.config.api/mapillary.config.api.general.md",tags:[],version:"current",frontMatter:{"sidebar position":3},sidebar:"tutorialSidebar",previous:{title:"mapillary.config.api.entities",permalink:"/mapillary-python-sdk/docs/mapillary.config.api/mapillary.config.api.entities"},next:{title:"mapillary.config.api",permalink:"/mapillary-python-sdk/docs/mapillary.config.api/mapillary.config.api"}},f=[{value:"mapillary.config.api.general",id:"mapillaryconfigapigeneral",children:[]},{value:"class mapillary.config.api.general.General()",id:"class-mapillaryconfigapigeneralgeneral",children:[]}],s={toc:f};function m(e){var t=e.components,a=(0,n.Z)(e,l);return(0,r.kt)("wrapper",(0,i.Z)({},s,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h3",{id:"mapillaryconfigapigeneral"},"mapillary.config.api.general"),(0,r.kt)("p",null,"This module contains the class implementation of the\ngeneral metadata functionalities for the API v4 of Mapillary."),(0,r.kt)("p",null,"For more information, please check out ",(0,r.kt)("a",{parentName:"p",href:"https://www.mapillary.com/developer/api-documentation/"},"https://www.mapillary.com/developer/api-documentation/"),"."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Copyright: (c) 2021 Facebook")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"License: MIT LICENSE")),(0,r.kt)("h3",{id:"class-mapillaryconfigapigeneralgeneral"},"class mapillary.config.api.general.General()"),(0,r.kt)("p",null,"Bases: ",(0,r.kt)("inlineCode",{parentName:"p"},"object")),(0,r.kt)("p",null,"A general list of metadata API endpoints for API v4"),(0,r.kt)("h4",{id:"static-get_computed_image_type_tilesx-float-y-float-z-float"},"static get_computed_image_type_tiles(x: float, y: float, z: float)"),(0,r.kt)("p",null,"Computed image_type tiles"),(0,r.kt)("h4",{id:"static-get_image_type_tilesx-float-y-float-z-float"},"static get_image_type_tiles(x: float, y: float, z: float)"),(0,r.kt)("p",null,"image_type tiles"),(0,r.kt)("h4",{id:"static-get_map_features_points_tilesx-float-y-float-z-float"},"static get_map_features_points_tiles(x: float, y: float, z: float)"),(0,r.kt)("p",null,"Map features (points) tiles"),(0,r.kt)("h4",{id:"static-get_map_features_traffic_signs_tilesx-float-y-float-z-float"},"static get_map_features_traffic_signs_tiles(x: float, y: float, z: float)"),(0,r.kt)("p",null,"Map features (traffic signs) tiles"),(0,r.kt)("h4",{id:"static-get_tile_metadata"},"static get_tile_metadata()"),(0,r.kt)("p",null,"Root endpoint for metadata"),(0,r.kt)("h4",{id:"static-get_vector_tiles"},"static get_vector_tiles()"),(0,r.kt)("p",null,"Root endpoint for vector tiles"))}m.isMDXComponent=!0}}]);