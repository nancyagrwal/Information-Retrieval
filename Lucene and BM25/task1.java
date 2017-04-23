import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.core.SimpleAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopScoreDocCollector;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;

public class HW4Task1 {
	
	// Index will be created at this location
	//private static String indexLocation = "C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\index\\";
	private static String indexLocation = "index\\";
	
	// html files from HW1
	//private static String dirToIndex = "C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\htmls" ;
	private static String dirToIndex = "htmls\\" ;
	
	private static Analyzer sAnalyzer = new SimpleAnalyzer(Version.LUCENE_47);
	private static List<File> fileList=new ArrayList<File>();
	private static String[] queries=new String[]{"light bulb bulbs alternative alternatives","solar energy california","green power renewable energy","global warming potential"};
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FSDirectory dir;
		IndexWriter writeIndex;
		try {
			dir = FSDirectory.open(new File(indexLocation));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("Cannot open the Directory specified at index location");
			return;
		}
		IndexWriterConfig config=new IndexWriterConfig(Version.LUCENE_47,sAnalyzer);
		try {
			 writeIndex=new IndexWriter(dir,config);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Failed to create index writer");
			e.printStackTrace();
			return;
			
		}
		listFiles(dirToIndex);
		indexFiles(fileList, writeIndex);
		try {
			searchQuery();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Cannot Search");
			e.printStackTrace();
		}
	}
	
	public static void listFiles(String dirName){
		
		File file=new File(dirName);
		if(file.isDirectory()){
			File[] files=file.listFiles();
			for(File f:files){
				listFiles(f.getAbsolutePath());
			}
		}
		else{
			fileList.add(file);
		}
	}
	
	public static void indexFiles(List<File> list,IndexWriter writer){
		for (File f : list) {
		    FileReader fileReader = null;
		    try {
			Document doc = new Document();

			
			fileReader = new FileReader(f);
			doc.add(new TextField("contents", fileReader));
			doc.add(new StringField("path", f.getPath(), Field.Store.YES));
			doc.add(new StringField("filename", f.getName(),
				Field.Store.YES));

			writer.addDocument(doc);
			System.out.println("Added: " + f);
		    } catch (Exception e) {
		    	e.printStackTrace();
			System.out.println("Could not add: " + f);
		    } finally {
			try {
				fileReader.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		    }
		}
		try {
			writer.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private static void searchQuery() throws IOException{
		
		
		for (String query:queries){
			IndexReader reader = DirectoryReader.open(FSDirectory.open(new File(indexLocation)));
			IndexSearcher searcher = new IndexSearcher(reader);
			TopScoreDocCollector collector = TopScoreDocCollector.create(100, true);
			Query q=null;
			try {
				q = new QueryParser(Version.LUCENE_47, "contents",sAnalyzer).parse(query);
			
			searcher.search(q, collector);
			} catch (ParseException e) {
				// TODO Auto-generated catch block
				System.out.println("Exception");
				e.printStackTrace();
			}
			catch(NullPointerException nullEx){
				nullEx.printStackTrace();
			}
			ScoreDoc[] totalMatches = collector.topDocs().scoreDocs;
			
			String searchFileName=query.replaceAll(" ", "_");
			//File file = new File("C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\results\\" + searchFileName+ ".txt");
			File file = new File("results\\" + searchFileName+ ".txt");
			file.createNewFile();
			BufferedWriter f=new BufferedWriter(new FileWriter(file));
			for(int i=0;i<totalMatches.length;i++){
				int documentId=totalMatches[i].doc;
				Document d = searcher.doc(documentId);
				String s=(i + 1) + ". " + d.get("path") + " score=" + totalMatches[i].score;
				f.write(s);
				f.newLine();
				
			}
			f.flush();
			f.close();
			
			
		}
		
	}

}
