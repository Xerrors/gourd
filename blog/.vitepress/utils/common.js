// 测试功能暂时先这样
export function getRandomCover() {
  return 'https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png';
}

export function getQueryVariable(variable){
  let query = window.location.search.substring(1);
  let vars = query.split("&");
  for (let i=0;i<vars.length;i++) {
          let pair = vars[i].split("=");
          if(pair[0] == variable){return pair[1];}
  }
  return(false);
}